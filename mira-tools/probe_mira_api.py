#!/usr/bin/env python3
"""Read-only Mira API health probe. No credentials, no mutations, no fake PASS.

Usage:
  python mira-tools/probe_mira_api.py --base-url https://zanistarast-papers.onrender.com
Exit: 0 only when /health returns expected service/status JSON; 2 otherwise.
"""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

EXPECTED_HOST = "zanistarast-papers.onrender.com"

def check(base_url, timeout=12):
    parsed = urllib.parse.urlparse(base_url)
    if parsed.scheme != "https" or parsed.hostname != EXPECTED_HOST or parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in ("", "/"):
        return {"status": "NOT_VERIFIED", "reason": "Unapproved API endpoint"}
    url = base_url.rstrip("/") + "/health"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"}, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = response.read(8193)
            if len(body) > 8192:
                return {"status": "NOT_VERIFIED", "reason": "Oversized response"}
            payload = json.loads(body)
            if response.status == 200 and payload.get("service") == "zanistarast-mira-api" and payload.get("status") == "ok":
                return {"status": "HEALTH_ENDPOINT_OK", "url": url, "note": "Health only; does not prove autonomous research or reviewer execution"}
            return {"status": "NOT_VERIFIED", "reason": "Unexpected health payload"}
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        return {"status": "NOT_VERIFIED", "reason": type(exc).__name__}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="https://" + EXPECTED_HOST)
    parser.add_argument("--timeout", type=int, default=12)
    args = parser.parse_args()
    result = check(args.base_url, args.timeout)
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0 if result["status"] == "HEALTH_ENDPOINT_OK" else 2)
