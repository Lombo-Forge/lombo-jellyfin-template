---
name: new-app-from-template
description: Turn this Lombo-Forge template into a new Jellyfin companion app. Use when the user wants to make their own app from the template, rename it, or replace the example rule. Removes itself after the rename.
---

# New app from the template

1. **Ask first, in plain words:** what should the app do, in one sentence? What should it be called
   (one lowercase word or a few joined by hyphens, e.g. `cleaner`)? What does it need from Jellyfin?
   Which alert, if any, do they want?
2. **Work in a fresh copy** with its own git history (never inside someone else's repo).
3. **Rename:** `python3 scripts/rename.py <name>`. It replaces the placeholders, renames the package,
   swaps in the app README and deletes the template-only files, including this skill.
4. **Write the rule, test first.** Replace `decide()` in `src/lombo_<name>/core.py`. Keep it pure
   (plain data in, plain data out). Write the failing test in `tests/` before the code.
5. **Add only the Jellyfin calls the rule needs** to `jellyfin.py`, with the matching path in the
   fake in `tests/conftest.py`.
6. **Keep safe defaults:** `DRY_RUN` true, `plan` changes nothing.
7. **Fill in** the README (one sentence, a screenshot of `plan`, the settings), `.env.example`
   (one comment line per setting) and `NOTICE.md`.
8. **Verify:** `pytest -q`, `sh scripts/leak-check.sh`, then `doctor` and `plan` against a throwaway
   Jellyfin container. Say plainly which of these you ran and which you could not.
9. **Branding:** follow `docs/branding.md` (the Lombo L in every icon) when making the icon and banner.

Do not add dependencies, a database or a web interface unless the user's rule cannot work without it.
