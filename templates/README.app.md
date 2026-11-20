<p align="center"><img src="assets/banner.svg" alt="LomboApp" width="100%"></p>

<p align="center">
  <a href="LICENSE"><img alt="License: GPL-3.0" src="https://img.shields.io/github/license/Lombo-Forge/lombo-app"></a>
  <a href="https://github.com/Lombo-Forge/lombo-app/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Lombo-Forge/lombo-app/ci.yml?branch=main&label=CI"></a>
  <a href="https://github.com/Lombo-Forge/lombo-app/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://img.shields.io/github/actions/workflow/status/Lombo-Forge/lombo-app/codeql.yml?branch=main&label=CodeQL"></a>
  <a href="https://github.com/Lombo-Forge/lombo-app/releases"><img alt="Release" src="https://img.shields.io/github/v/release/Lombo-Forge/lombo-app?include_prereleases"></a>
  <img alt="Python 3.12+" src="https://img.shields.io/badge/python-3.12%2B-blue">
</p>

# LomboApp

One sentence on what it does, for someone who has never heard of it.

<!-- screenshot or terminal output of `plan` here -->

## Contents

- [Install in a minute](#install-in-a-minute)
- [Commands](#commands)
- [Settings](#settings)
- [FAQ](#faq)
- [Contributing and licence](#contributing-and-licence)

## Install in a minute

1. In Jellyfin, open Dashboard > API Keys and create a key for LomboApp.
2. Copy `.env.example` to `.env` and fill in the URL and key.
3. Start it:
   ```sh
   docker compose -f compose.example.yaml up -d
   docker compose -f compose.example.yaml exec lombo-app lombo-app doctor
   ```

It starts in dry-run mode and changes nothing. Run `lombo-app plan` to see what it would do, then set `LOMBO_APP_DRY_RUN=false` when you are happy.

## Commands

| Command | What it does |
|---|---|
| `lombo-app doctor` | Checks your settings and that Jellyfin answers. Exit code 1 if anything fails. |
| `lombo-app plan` | Shows what would happen. Never changes anything. |
| `lombo-app run [--loop]` | Does it. `--loop` repeats every `LOMBO_APP_INTERVAL_SECONDS`. |

## Settings

Everything is an environment variable, listed with defaults in [.env.example](.env.example).

## FAQ

**Is it safe to try?** Yes. Dry run is the default.

## Contributing and licence

Contribution, security and conduct rules come from the [Lombo-Forge organisation](https://github.com/Lombo-Forge/.github). Licensed under [GPL-3.0](LICENSE). Credits are in [NOTICE.md](NOTICE.md). Not affiliated with or endorsed by the Jellyfin project.
