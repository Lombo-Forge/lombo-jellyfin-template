"""A small Jellyfin client, standard library only. Add the calls your app needs here.

Authentication uses an API key (Jellyfin: Dashboard > API Keys) in the Authorization header.
Every failure becomes a JellyfinError with a short message, so callers print it instead of crashing.
"""
import json
import urllib.error
import urllib.request


class JellyfinError(Exception):
    """A request failed. The message names the path and the reason."""


class Jellyfin:
    def __init__(self, base_url: str, api_key: str, timeout: float = 10):
        self.base = base_url.rstrip("/")
        self.key = api_key
        self.timeout = timeout

    def _get(self, path: str, auth: bool = True):
        req = urllib.request.Request(self.base + path)
        if auth:
            req.add_header("Authorization", f'MediaBrowser Token="{self.key}"')
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            raise JellyfinError(f"{path}: HTTP {e.code}") from e
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise JellyfinError(f"{path}: {e}") from e

    def public_info(self) -> dict:
        """Server name and version. Needs no key, so it tells 'unreachable' apart from 'bad key'."""
        return self._get("/System/Info/Public", auth=False)

    def info(self) -> dict:
        """Needs a valid key."""
        return self._get("/System/Info")

    def libraries(self) -> list[dict]:
        return self._get("/Library/VirtualFolders")
