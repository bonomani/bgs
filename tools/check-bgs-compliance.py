#!/usr/bin/env python3
"""BGS compliance checker.

Validates a project's BGS entry file and decision record against
BGS-COMPLIANCE.md rules. Exit 0 on pass, non-zero on failure.

Usage:
    python check-bgs-compliance.py [BGS_ENTRY_PATH] [--max-staleness DAYS]

Defaults:
    BGS_ENTRY_PATH: ./BGS.md
    --max-staleness: 90
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


VALID_SLICES = {
    "BGS-Classification",
    "BGS-Foundation",
    "BGS-Execution",
    "BGS-Governed",
    "BGS-Verified",
    "BGS-Governed-Verified",
    "BGS-State-Modeled-Execution",
    "BGS-State-Modeled-Governed",
    "BGS-State-Modeled-Governed-Verified",
}

SLICE_REQUIRED_MEMBERS: dict[str, set[str]] = {
    "BGS-Classification": {"BISS"},
    "BGS-Foundation": set(),
    "BGS-Execution": {"BISS", "UCC"},
    "BGS-Governed": {"BISS", "UIC", "UCC"},
    "BGS-Verified": {"BISS", "UCC", "TIC"},
    "BGS-Governed-Verified": {"BISS", "UIC", "UCC", "TIC"},
    "BGS-State-Modeled-Execution": {"BISS", "ASM", "UCC"},
    "BGS-State-Modeled-Governed": {"BISS", "ASM", "UIC", "UCC"},
    "BGS-State-Modeled-Governed-Verified": {"BISS", "ASM", "UIC", "UCC", "TIC"},
}

REQUIRED_DECISION_FIELDS = {
    "decision_id",
    "bgs_slice",
    "declared_scope",
    "bgs_version_ref",
    "members_used",
    "overlays_used",
    "member_version_refs",
    "external_controls",
    "evidence_refs",
}

REQUIRED_ENTRY_FIELDS = {
    "project_name",
    "bgs_slice",
    "decision_reason",
    "applies_to_scope",
    "decision_record_path",
    "last_reviewed",
    "read_next",
}

BRANCH_PATTERN = re.compile(r"^(main|master|develop|HEAD)$")


def parse_simple_yaml_frontmatter(text: str) -> dict[str, Any]:
    """Parse simple key: value pairs and list fields from markdown content."""
    result: dict[str, Any] = {}
    current_key: str | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            current_key = None
            continue
        if stripped.startswith("- ") and current_key is not None:
            value = stripped[2:].strip().strip('"').strip("'")
            if isinstance(result.get(current_key), list):
                result[current_key].append(value)
            else:
                result[current_key] = [value]
            continue
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key:
                current_key = key
                if value:
                    result[key] = value
                else:
                    result[key] = []
    return result


def load_yaml_file(path: Path) -> dict[str, Any]:
    """Load a YAML file, trying PyYAML first then falling back to JSON."""
    text = path.read_text(encoding="utf-8")
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ImportError:
        pass
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return parse_simple_yaml_frontmatter(text)


def check_entry_file(path: Path) -> list[str]:
    """Check BGS entry file for required fields."""
    errors: list[str] = []
    if not path.exists():
        errors.append(f"BGS entry file not found: {path}")
        return errors
    data = parse_simple_yaml_frontmatter(path.read_text(encoding="utf-8"))
    for field in REQUIRED_ENTRY_FIELDS:
        if field not in data:
            errors.append(f"entry: missing required field '{field}'")
    bgs_slice = data.get("bgs_slice", "")
    if bgs_slice and bgs_slice not in VALID_SLICES:
        errors.append(f"entry: '{bgs_slice}' is not a valid claimable BGS slice")
    return errors


def check_decision_record(path: Path, base_dir: Path) -> list[str]:
    """Check decision record for required fields and validity."""
    errors: list[str] = []
    if not path.exists():
        errors.append(f"decision record not found: {path}")
        return errors
    data = load_yaml_file(path)
    for field in REQUIRED_DECISION_FIELDS:
        if field not in data:
            errors.append(f"decision: missing required field '{field}'")

    bgs_slice = data.get("bgs_slice", "")
    if bgs_slice and bgs_slice not in VALID_SLICES:
        errors.append(f"decision: '{bgs_slice}' is not a valid claimable BGS slice")

    members = set(data.get("members_used", []))
    required = SLICE_REQUIRED_MEMBERS.get(bgs_slice, set())
    missing = required - members
    if missing:
        errors.append(f"decision: slice '{bgs_slice}' requires members {sorted(missing)}")

    refs = data.get("member_version_refs", {})
    if isinstance(refs, dict):
        for name, ref in refs.items():
            ref_str = str(ref)
            if BRANCH_PATTERN.match(ref_str):
                errors.append(f"decision: member_version_ref '{name}: {ref_str}' is a branch name, not an immutable ref")

    bgs_ref = str(data.get("bgs_version_ref", ""))
    if bgs_ref and BRANCH_PATTERN.match(bgs_ref.split("@")[-1] if "@" in bgs_ref else bgs_ref):
        errors.append(f"decision: bgs_version_ref '{bgs_ref}' is not an immutable ref")

    evidence = data.get("evidence_refs", [])
    if isinstance(evidence, list):
        for ref in evidence:
            ref_path = base_dir / str(ref)
            if not ref_path.exists():
                errors.append(f"decision: evidence_ref not found: {ref}")

    return errors


def check_staleness(path: Path, max_days: int) -> list[str]:
    """Check if last_reviewed is within acceptable range."""
    errors: list[str] = []
    data = parse_simple_yaml_frontmatter(path.read_text(encoding="utf-8"))
    reviewed = data.get("last_reviewed", "")
    if not reviewed:
        errors.append("entry: 'last_reviewed' is missing or empty")
        return errors
    try:
        reviewed_date = datetime.strptime(reviewed, "%Y-%m-%d")
        if datetime.now() - reviewed_date > timedelta(days=max_days):
            errors.append(f"entry: last_reviewed '{reviewed}' is older than {max_days} days")
    except ValueError:
        errors.append(f"entry: last_reviewed '{reviewed}' is not a valid YYYY-MM-DD date")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="BGS compliance checker")
    parser.add_argument("entry", nargs="?", default="./BGS.md", help="Path to BGS entry file")
    parser.add_argument("--max-staleness", type=int, default=90, help="Max days since last_reviewed")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    entry_path = Path(args.entry).resolve()
    base_dir = entry_path.parent
    errors: list[str] = []

    errors.extend(check_entry_file(entry_path))

    if entry_path.exists():
        data = parse_simple_yaml_frontmatter(entry_path.read_text(encoding="utf-8"))
        decision_path_str = data.get("decision_record_path", "")
        if decision_path_str:
            decision_path = (base_dir / decision_path_str).resolve()
            errors.extend(check_decision_record(decision_path, base_dir))
        else:
            errors.append("entry: 'decision_record_path' is missing")
        errors.extend(check_staleness(entry_path, args.max_staleness))

    if args.json:
        result = {"pass": len(errors) == 0, "errors": errors}
        print(json.dumps(result, indent=2))
    else:
        if errors:
            for err in errors:
                print(f"FAIL: {err}")
        else:
            print("PASS: BGS compliance check passed")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
