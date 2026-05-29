#!/usr/bin/env python3
"""Validate the Evolutionary Origin Ontology JSONL dataset.

This validator uses only the Python Standard Library.

It checks that every non-empty JSONL line is a JSON object with exactly two
string fields:

- instruction
- output

Usage:

    python validate.py
    python validate.py data/train.jsonl
    python validate.py data/train.jsonl --expected-count 500
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Iterable, Set, Tuple


REQUIRED_KEYS = {"instruction", "output"}
DEFAULT_DATASET_PATH = Path("data") / "train.jsonl"


class ValidationError(Exception):
    """Raised when dataset validation fails."""


def validate_record(record: object, *, path: Path, line_number: int) -> Dict[str, str]:
    """Validate one parsed JSONL record."""

    if not isinstance(record, dict):
        raise ValidationError(
            f"{path}:{line_number}: expected a JSON object, got {type(record).__name__}."
        )

    keys = set(record.keys())

    if keys != REQUIRED_KEYS:
        missing = sorted(REQUIRED_KEYS - keys)
        extra = sorted(keys - REQUIRED_KEYS)
        details = []

        if missing:
            details.append(f"missing={missing}")
        if extra:
            details.append(f"extra={extra}")

        raise ValidationError(
            f"{path}:{line_number}: record must contain exactly "
            f"{sorted(REQUIRED_KEYS)} ({', '.join(details)})."
        )

    instruction = record["instruction"]
    output = record["output"]

    if not isinstance(instruction, str):
        raise ValidationError(
            f"{path}:{line_number}: `instruction` must be string, "
            f"got {type(instruction).__name__}."
        )

    if not isinstance(output, str):
        raise ValidationError(
            f"{path}:{line_number}: `output` must be string, "
            f"got {type(output).__name__}."
        )

    if not instruction.strip():
        raise ValidationError(f"{path}:{line_number}: `instruction` cannot be empty.")

    if not output.strip():
        raise ValidationError(f"{path}:{line_number}: `output` cannot be empty.")

    return {"instruction": instruction, "output": output}


def validate_file(
    path: Path,
    *,
    strict_instruction_prefix: bool = False,
) -> Tuple[int, Set[str]]:
    """Validate one JSONL file."""

    if not path.exists():
        raise ValidationError(f"{path}: file does not exist.")

    if not path.is_file():
        raise ValidationError(f"{path}: path is not a file.")

    count = 0
    instructions: Set[str] = set()

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()

            if not line:
                continue

            try:
                parsed = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValidationError(
                    f"{path}:{line_number}: invalid JSON: {exc.msg}."
                ) from exc

            record = validate_record(parsed, path=path, line_number=line_number)
            instruction = record["instruction"]

            if strict_instruction_prefix and not instruction.startswith(
                "Resolve the systemic distortion of "
            ):
                raise ValidationError(
                    f"{path}:{line_number}: instruction does not use the required prefix."
                )

            if instruction in instructions:
                raise ValidationError(
                    f"{path}:{line_number}: duplicate instruction detected: "
                    f"{instruction!r}."
                )

            instructions.add(instruction)
            count += 1

    if count == 0:
        raise ValidationError(f"{path}: no records found.")

    return count, instructions


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Validate the Evolutionary Origin Ontology JSONL dataset."
    )

    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(DEFAULT_DATASET_PATH)],
        help="JSONL file path(s) to validate. Defaults to data/train.jsonl.",
    )

    parser.add_argument(
        "--expected-count",
        type=int,
        default=None,
        help="Expected total number of records across all provided files.",
    )

    parser.add_argument(
        "--strict-instruction-prefix",
        action="store_true",
        help="Require each instruction to begin with 'Resolve the systemic distortion of '.",
    )

    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    """Run validation and return a process exit code."""

    args = parse_args(argv)
    paths = [Path(path) for path in args.paths]

    total_count = 0
    global_instructions: Set[str] = set()

    try:
        for path in paths:
            count, instructions = validate_file(
                path,
                strict_instruction_prefix=args.strict_instruction_prefix,
            )

            duplicates_across_files = global_instructions.intersection(instructions)

            if duplicates_across_files:
                duplicate = sorted(duplicates_across_files)[0]
                raise ValidationError(
                    f"{path}: duplicate instruction across files: {duplicate!r}."
                )

            global_instructions.update(instructions)
            total_count += count

            print(f"✓ {path}: {count} records valid")

        if args.expected_count is not None and total_count != args.expected_count:
            raise ValidationError(
                f"expected {args.expected_count} total records, found {total_count}."
            )

    except ValidationError as exc:
        print(f"✗ Validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"✓ Validation passed: {total_count} total records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
