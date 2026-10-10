"""Regression tests for the offline Mira evidence gate.

Run in an isolated checkout:
    python -m unittest discover -s mira-tools -p 'test_*.py'
"""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("gate", Path(__file__).with_name("review_evidence_gate.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

def record(reviewer, round_number):
    return {
        "reviewer_id": reviewer,
        "round": round_number,
        "verdict": "major_revision" if round_number == 1 else "minor_revision",
        "evidence": ["artifact:source:line"],
        "concerns": ["methodology"] if round_number == 1 else [],
        "responses": [] if round_number == 1 else ["revision:methodology"],
        "run_id": f"run-{reviewer}-{round_number}",
        "artifact_uri": f"artifact://{reviewer}/{round_number}",
    }

def complete():
    return {
        "manuscript_id": "sample-not-a-real-paper",
        "target_journal": "example-journal",
        "revision_artifact_uri": "artifact://revision/v2",
        "reviews": [record(r, t) for r in gate.REVIEWERS for t in (1, 2)],
    }

class EvidenceGateTests(unittest.TestCase):
    def test_complete_evidence(self):
        self.assertEqual(gate.validate(complete()), [])

    def test_missing_second_round_is_rejected(self):
        data = complete()
        data["reviews"] = [r for r in data["reviews"] if r["round"] == 1]
        self.assertTrue(any("missing independent" in e for e in gate.validate(data)))

    def test_duplicate_reviewer_is_rejected(self):
        data = complete()
        data["reviews"].append(data["reviews"][0])
        self.assertTrue(any("duplicate" in e for e in gate.validate(data)))

    def test_missing_source_is_rejected(self):
        data = complete()
        data["reviews"][0]["evidence"] = []
        self.assertTrue(any("evidence required" in e for e in gate.validate(data)))

    def test_missing_revision_is_rejected(self):
        data = complete()
        del data["revision_artifact_uri"]
        self.assertTrue(any("revision_artifact_uri" in e for e in gate.validate(data)))

if __name__ == "__main__":
    unittest.main()
