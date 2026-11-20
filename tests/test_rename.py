"""Keeps the template renamable: a copy renamed to 'demo' must be clean, and its own tests must pass."""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_rename_produces_a_clean_working_app(tmp_path):
    copy = tmp_path / "demo"
    shutil.copytree(
        ROOT,
        copy,
        ignore=shutil.ignore_patterns(
            ".git",
            "__pycache__",
            ".pytest_cache",
            ".ruff_cache",
            ".mypy_cache",
            ".coverage",
            "graphify-out",
            "*.egg-info",
        ),
    )
    done = subprocess.run([sys.executable, "scripts/rename.py", "demo"], cwd=copy, capture_output=True, text=True)
    assert done.returncode == 0, done.stderr

    leftovers = [
        str(p.relative_to(copy))
        for p in copy.rglob("*")
        if p.is_file()
        and re.search(r"lombo_app|lombo-app|LomboApp|LOMBO_APP|template:begin", p.read_text(errors="ignore"))
    ]
    assert leftovers == []
    assert (copy / "src" / "lombo_demo" / "core.py").exists()
    assert not (copy / "scripts" / "rename.py").exists()
    assert not (copy / "templates").exists()
    assert "LomboDemo" in (copy / "README.md").read_text()

    tests = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"], cwd=copy, capture_output=True, text=True
    )
    assert tests.returncode == 0, tests.stdout + tests.stderr
