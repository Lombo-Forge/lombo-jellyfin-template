# Using this template

## Contents

- [Before you start](#before-you-start)
- [Make your app](#make-your-app)
- [Write the rules](#write-the-rules)
- [Check it against Jellyfin](#check-it-against-jellyfin)
- [Make it yours](#make-it-yours)
- [Publish](#publish)

## Before you start

You need Python 3.12 or newer (or Docker), git, and a Jellyfin server you can safely test against.
Use a throwaway Jellyfin container for development. These apps can alert, stop or move things, so
never point an unfinished one at the server your family uses.

## Make your app

1. On GitHub choose **Use this template**, or clone it and delete `.git`, then `git init`. Either
   way your app starts with its own fresh history.
2. Run `python3 scripts/rename.py <name>`. For `cleaner` you get `lombo-cleaner`, the package
   `lombo_cleaner`, the display name `LomboCleaner` and settings starting `LOMBO_CLEANER_`. If the
   app is not part of Lombo-Forge, edit the prefix text afterwards; the script only knows the
   Lombo pattern.
3. The script removes the template-only files (itself, the template README, this page, the
   rename test and the new-app skill), so what is left is your app.

## Write the rules

Open `src/lombo_<name>/core.py`. The example flags libraries with no folders. Replace `decide()`
with your rule. Write the test first in `tests/`, using plain data, then make it pass. If the rule
needs something from Jellyfin that the client lacks, add a method to `jellyfin.py` and the matching
path to the fake in `tests/conftest.py`.

## Check it against Jellyfin

1. Start a throwaway Jellyfin and create an API key (Dashboard, API Keys).
2. Fill in `.env`, then run `doctor` and `plan`.
3. Only then set `DRY_RUN=false`, still on the throwaway server.

The fake server in the tests is a convenience, not proof. Real Jellyfin versions differ, so confirm
every call you add.

## Make it yours

- Icon, banner and social preview: see [branding.md](branding.md).
- Fill in the README top (one sentence, a screenshot of `plan`) and the FAQ.
- Add third-party credits to `NOTICE.md`.
- Run `sh scripts/leak-check.sh` and add your own private strings to `scripts/leak-patterns.txt`.

## Publish

1. Push to GitHub and check that CI is green.
2. Tag a release (`git tag v0.1.0 && git push --tags`). The release workflow publishes the image.
3. Add the topics `jellyfin` and `selfhosted` so people can find it.
