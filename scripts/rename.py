#!/usr/bin/env python3
"""Turn this template into a new app:  python3 scripts/rename.py tier  ->  lombo-tier / LomboTier.

Replaces the placeholder names everywhere, renames the package folder, swaps in the app README
(templates/README.app.md), removes the template-only notes, then deletes itself. Run it once, in a
fresh copy, before anything else. Needs only Python 3.
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "node_modules",
    "graphify-out",
    ".venv",
    "dist",
    "build",
    ".tox",
}
TEMPLATE_ONLY = [
    "scripts/rename.py",
    "templates",
    "docs/using-this-template.md",
    "tests/test_rename.py",
    ".claude/skills/new-app-from-template",
]


def names(slug: str) -> dict[str, str]:
    snake = slug.replace("-", "_")
    return {
        "LOMBO_APP": f"LOMBO_{snake.upper()}",
        "lombo_app": f"lombo_{snake}",
        "lombo-app": f"lombo-{slug}",
        "LomboApp": "Lombo" + "".join(p.capitalize() for p in slug.split("-")),
    }


def main(argv: list[str]) -> int:
    keep = "--keep-template-files" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", args[0]):
        print(
            "usage: python3 scripts/rename.py <name> [--keep-template-files]\n"
            "name: lowercase letters, digits and hyphens, e.g. tier or media-cleaner",
            file=sys.stderr,
        )
        return 2
    new = names(args[0])

    if not keep:
        app_readme = ROOT / "templates" / "README.app.md"
        if app_readme.exists():
            shutil.move(app_readme, ROOT / "README.md")
        for rel in TEMPLATE_ONLY:
            p = ROOT / rel
            shutil.rmtree(p) if p.is_dir() else p.unlink(missing_ok=True)

    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # images and other binaries
        out = text
        for old, repl in new.items():
            out = out.replace(old, repl)
        if not keep:
            out = re.sub(r"<!-- template:begin -->.*?<!-- template:end -->\n?", "", out, flags=re.S)
        if out != text:
            path.write_text(out, encoding="utf-8")

    pkg = ROOT / "src" / "lombo_app"
    if pkg.exists():
        pkg.rename(ROOT / "src" / new["lombo_app"])
    print(
        f"Renamed to {new['lombo-app']} ({new['LomboApp']}). Next: replace decide() in "
        f"src/{new['lombo_app']}/core.py, then run the tests."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
