#!/usr/bin/env python3
"""Safe, offline evidence gate for Mira's 3-reviewer / 2-round process.

This validates *supplied* review records. It does not run an LLM, claim
independent reviewers, or connect to a live PWA/Render service.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REVIEWERS = ("target_journal", "cross_journal", "independent_critical")
VERDICTS = {"accept", "minor_revision", "major_revision", "reject"}
FIELDS = ("reviewer_id", "round", "verdict", "evidence", "concerns", "responses")

def validate(payload):
    errors = []
    if not isinstance(payload, dict):
        return ["Input must be an object"]
    if not payload.get("manuscript_id") or not payload.get("target_journal"):
        errors.append("manuscript_id and target_journal are required")
    records = payload.get("reviews", [])
    if not isinstance(records, list):
        return errors + ["reviews must be an array"]
    seen = set()
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            errors.append(f"reviews[{i}] must be an object")
            continue
        missing = [k for k in FIELDS if k not in rec]
        if missing:
            errors.append(f"reviews[{i}] missing: {', '.join(missing)}")
            continue
        key = (rec["reviewer_id"], rec["round"])
        if key in seen:
            errors.append(f"duplicate reviewer-round: {key}")
        seen.add(key)
        if rec["reviewer_id"] not in REVIEWERS or rec["round"] not in (1, 2):
            errors.append(f"invalid reviewer or round at {i}")
        if rec["verdict"] not in VERDICTS:
            errors.append(f"invalid verdict at {i}")
        if not isinstance(rec["evidence"], list) or not rec["evidence"]:
            errors.append(f"evidence required at {i}")
        if not isinstance(rec["concerns"], list) or not isinstance(rec["responses"], list):
            errors.append(f"concerns/responses must be arrays at {i}")
        if not rec.get("run_id") or not rec.get("artifact_uri"):
            errors.append(f"run_id and artifact_uri required at {i}")
    required = {(r, t) for r in REVIEWERS for t in (1, 2)}
    missing_pairs = sorted(required - seen)
    if missing_pairs:
        errors.append(f"missing independent review records: {missing_pairs}")
    if not payload.get("revision_artifact_uri"):
        errors.append("revision_artifact_uri required between rounds")
    return errors

def run(input_file, output_dir):
    raw = Path(input_file).read_bytes()
    payload = json.loads(raw)
    errors = validate(payload)
    result = {
        "schema": "mira-review-evidence-gate-v1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "status": "EVIDENCE_COMPLETE" if not errors else "NOT_VERIFIED",
        "errors": errors,
        "note": "Validates records only; no journal acceptance or reviewer independence proven.",
    }
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    name = "gate-" + result["input_sha256"][:16] + ".json"
    target = directory / name
    with target.open("x", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    assert json.loads(target.read_text(encoding="utf-8")) == result
    return result, target

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    result, target = run(args.input, args.output_dir)
    print(json.dumps({"status": result["status"], "artifact": str(target), "errors": result["errors"]}, ensure_ascii=False))
    raise SystemExit(0 if not result["errors"] else 2)
