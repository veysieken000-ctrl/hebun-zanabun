#!/usr/bin/env python3
"""
Governance Simulation Prototype
Generates concentration risk metrics (C, T_avg, O, I) and R_c score.

Design goal: simple, transparent, dependency-free.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Member:
    id: str
    tenure_periods: int = 0


@dataclass
class Council:
    name: str
    base_power: float
    members: List[Member]


def load_config(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg


def band(r_c: float, thresholds: Dict[str, float]) -> str:
    safe = thresholds["safe"]
    warning = thresholds["warning"]
    breach = thresholds["breach"]
    if r_c < safe:
        return "SAFE"
    if r_c < warning:
        return "WATCH"
    if r_c < breach:
        return "WARNING"
    return "BREACH"


def centralization_ratio(councils: List[Council], council_power: Dict[str, float]) -> float:
    total = sum(council_power[c.name] for c in councils)
    if total <= 0:
        return 0.0
    mx = max(council_power[c.name] for c in councils)
    return mx / total


def avg_tenure(councils: List[Council]) -> float:
    tenures = []
    for c in councils:
        for m in c.members:
            tenures.append(m.tenure_periods)
    return sum(tenures) / len(tenures) if tenures else 0.0


def opacity_index(n_total: int, n_public: int) -> float:
    if n_total <= 0:
        return 0.0
    return 1.0 - (n_public / n_total)


def overlap_ratio(councils: List[Council], allow_overlap: bool) -> float:
    if not allow_overlap:
        return 0.0
    # Count members that appear in more than one council by id
    seen = {}
    for c in councils:
        for m in c.members:
            seen[m.id] = seen.get(m.id, 0) + 1
    overlaps = sum(1 for _, k in seen.items() if k > 1)
    total = len(seen)
    return (overlaps / total) if total else 0.0


def compute_risk(C: float, T_avg: float, O: float, I: float, weights: Dict[str, float], tenure_max: int) -> float:
    # Normalize T_avg into [0,1] using tenure_max_periods
    Tn = min(1.0, (T_avg / tenure_max) if tenure_max > 0 else 0.0)
    r = (
        weights["w_C"] * C +
        weights["w_T"] * Tn +
        weights["w_O"] * O +
        weights["w_I"] * I
    )
    # Clamp for safety
    return max(0.0, min(1.0, r))


def rotate_members(council: Council, renewal_rate: float, next_member_id: int) -> int:
    """
    Replace a fraction of members with new members.
    """
    n = len(council.members)
    k = max(0, min(n, int(round(n * renewal_rate))))
    if k == 0:
        return next_member_id
    # Choose k members to replace
    idxs = random.sample(range(n), k)
    for idx in idxs:
        council.members[idx] = Member(id=f"m{next_member_id}", tenure_periods=0)
        next_member_id += 1
    return next_member_id


def inject_overlap(councils: List[Council], injection_rate: float) -> None:
    """
    Create overlap by copying some member IDs across councils (capture bridge simulation).
    This is intentionally simple.
    """
    if injection_rate <= 0:
        return
    all_members = [m for c in councils for m in c.members]
    if not all_members:
        return
    for c in councils:
        n = len(c.members)
        k = max(0, min(n, int(round(n * injection_rate))))
        if k == 0:
            continue
        chosen = random.sample(all_members, k)
        # overwrite some member ids to match chosen ones (simulates cross-membership)
        idxs = random.sample(range(n), k)
        for idx, src in zip(idxs, chosen):
            c.members[idx].id = src.id


def simulate(cfg: Dict) -> None:
    random.seed()

    councils_cfg = cfg["councils"]
    members_per_council = int(cfg["members_per_council"])
    periods = int(cfg["periods"])
    decisions_per_period = int(cfg["decisions_per_period"])
    documentation_rate = float(cfg["documentation_rate"])
    renewal_rate = float(cfg["renewal_rate_per_period"])
    allow_overlap = bool(cfg["allow_overlap"])
    overlap_injection_rate = float(cfg.get("overlap_injection_rate", 0.0))
    weights = cfg["weights"]
    thresholds = cfg["thresholds"]
    tenure_max = int(cfg.get("tenure_max_periods", 24))

    councils: List[Council] = []
    member_id_counter = 1

    for c in councils_cfg:
        members = []
        for _ in range(members_per_council):
            members.append(Member(id=f"m{member_id_counter}", tenure_periods=0))
            member_id_counter += 1
        councils.append(Council(name=c["name"], base_power=float(c["power"]), members=members))

    print("\n=== Governance Simulation Report ===\n")

    for p in range(1, periods + 1):
        # Member tenure increments
        for c in councils:
            for m in c.members:
                m.tenure_periods += 1

        # Rotation / renewal
        for c in councils:
            member_id_counter = rotate_members(c, renewal_rate, member_id_counter)

        # Optional overlap injection
        if allow_overlap and overlap_injection_rate > 0:
            inject_overlap(councils, overlap_injection_rate)

        # Simulate decisions and documentation
        n_total = decisions_per_period
        n_public = 0

        # Council decision power could drift; here we keep base power but allow slight random noise
        council_power: Dict[str, float] = {}
        for c in councils:
            noise = random.uniform(0.95, 1.05)
            council_power[c.name] = max(0.0, c.base_power * noise)

        for _ in range(n_total):
            if random.random() < documentation_rate:
                n_public += 1

        # Metrics
        C = centralization_ratio(councils, council_power)
        T_avg = avg_tenure(councils)
        O = opacity_index(n_total, n_public)
        I = overlap_ratio(councils, allow_overlap)
        R_c = compute_risk(C, T_avg, O, I, weights, tenure_max)
        status = band(R_c, thresholds)

        # Print period report
        print(f"Period {p}")
        print("Power distribution:")
        total_power = sum(council_power.values()) or 1.0
        for c in councils:
            share = council_power[c.name] / total_power
            print(f" - {c.name}: power={council_power[c.name]:.3f} share={share:.3f}")
        print("Metrics:")
        print(f" C (centralization) = {C:.3f}")
        print(f" T_avg (tenure avg) = {T_avg:.2f} periods")
        print(f" O (opacity index) = {O:.3f} (public {n_public}/{n_total})")
        print(f" I (overlap ratio) = {I:.3f}")
        print(f" R_c (risk score) = {R_c:.3f} => {status}")
        print("-" * 40)

    print("\n=== End of Report ===\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config JSON file.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    simulate(cfg)


if __name__ == "__main__":
    main()


