# AGENTS.md

Notes for an AI coding agent (or a person) working in this repo. `CLAUDE.md` pulls this file in.

<!-- template:begin -->
**This is the Lombo-Forge template.** To make a new app from it, follow
`.claude/skills/new-app-from-template/SKILL.md` and nothing else first. The rest of this file
describes the app you end up with.
<!-- template:end -->

## What this is

LomboApp is a small Python 3.12 program that runs beside a Jellyfin server and does one job.
Standard library only (add a dependency only when it clearly earns its place).

## Layout

| Path | What |
|---|---|
| `src/lombo_app/core.py` | The decisions. Pure functions: no network, disk or clock. Change the rules here. |
| `src/lombo_app/jellyfin.py` | The Jellyfin client. Add calls here. |
| `src/lombo_app/cli.py` | `doctor`, `plan`, `run`. The only place that does I/O and prints. |
| `src/lombo_app/config.py` | Settings from `LOMBO_APP_*` environment variables. |
| `src/lombo_app/notify.py` | Webhook alerts. |
| `tests/` | pytest, with a fake Jellyfin and webhook in `conftest.py`. |
| `scripts/leak-check.sh` | Fails when private or personal strings appear. CI runs it. |
| `docs/` | One topic per file, each with a `## Contents` list. |

## Rules

- **Keep `core.py` pure.** If a rule needs data, pass it in. That is what makes it testable.
- **Safe by default.** `DRY_RUN` defaults to true. `plan` must never change anything.
- **A new setting** goes in `config.py` (validated, message names the variable), `.env.example`
  (one comment line), and `compose.example.yaml` if it needs passing through.
- **Fail with a message, not a traceback.** Wrap outside calls; the loop survives one bad round.
- **Never put private details in the repo:** real hostnames, IPs, webhook URLs, API keys, local
  paths. Use `jellyfin.example.com`, `/mnt/media`, `changeme`. `scripts/leak-check.sh` enforces it;
  patterns live in `scripts/leak-patterns.txt`.
- Plain language in docs and messages. Call a PC used for encoding a "main PC with a discrete
  graphics card". Never call anything "official" or imply the Jellyfin project made it.
- The Lombo look (every icon has the Lombo L) is in `docs/branding.md`.

## Test

```sh
pip install -e '.[dev]' && pytest -q
sh scripts/leak-check.sh
```

Without Python installed: `docker run --rm -v "$PWD:/w" -w /w python:3.12-slim sh -c "pip install -q -e '.[dev]' && pytest -q"`.
Tests use a fake server; before claiming a Jellyfin behaviour works, check it against a throwaway
Jellyfin container, never someone's real server.

## Skills (`.claude/skills/`)

- `install-into-my-stack`: help a user put the app into their setup and run `doctor`.
- `troubleshoot`: read `doctor` output and logs.
- `adapt`: change the rules, thresholds or settings safely.
