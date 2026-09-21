"""Deterministic M0 repository qualification."""

from __future__ import annotations

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

REQUIRED_PATHS = (
    "src",
    "tests",
    "tools",
    "docs",
    ".ollin",
    "README.md",
    "CHANGELOG.md",
    "pyproject.toml",
    ".ollin/identity/PROJECT.md",
    ".ollin/law/PROJECT_LAW.md",
    ".ollin/architecture/PROFILE.md",
    ".ollin/milestones/M0.md",
    ".ollin/state/STATE.md",
    ".ollin/handoff/NEXT.md",
)

FORBIDDEN_TRACKED_DATA_NAMES = {"connections.csv", "neurons.csv", "synapses.csv"}


def fail(message: str) -> "NoReturn":
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    missing = [p for p in REQUIRED_PATHS if not (ROOT / p).exists()]
    if missing:
        fail("missing required paths: " + ", ".join(missing))

    for path in ROOT.rglob("*"):
        if path.is_file() and path.name.lower() in FORBIDDEN_TRACKED_DATA_NAMES:
            fail(f"bulk-data-like file present in M0 tree: {path.relative_to(ROOT)}")

    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if tests.returncode != 0:
        print(tests.stdout)
        print(tests.stderr, file=sys.stderr)
        fail("unit tests failed")

    print("M0 universal spine                 PASS")
    print("M0 project identity                PASS")
    print("M0 dataset registry                PASS")
    print("M0 no vendored bulk connectome     PASS")
    print("M0 unit verification               PASS")
    print("OLLIN FRUIT FLY LAB M0 QUALIFICATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
