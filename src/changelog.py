"""Fetch and parse the Claude Code changelog."""
from __future__ import annotations

import re
from dataclasses import dataclass

import requests

DEFAULT_URL = (
    "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
)
_VERSION_RE = re.compile(r"^##\s+\[?v?(\d+\.\d+\.\d+[^\]\s]*)\]?", re.MULTILINE)


@dataclass(frozen=True)
class Release:
    version: str
    notes: str


def fetch_changelog(url: str = DEFAULT_URL, *, http_get=requests.get) -> str:
    response = http_get(url, timeout=30)
    response.raise_for_status()
    return response.text


def parse_latest(text: str) -> Release:
    matches = list(_VERSION_RE.finditer(text))
    if not matches:
        raise ValueError("No version heading found in changelog")
    first = matches[0]
    start = first.end()
    end = matches[1].start() if len(matches) > 1 else len(text)
    return Release(version=first.group(1), notes=text[start:end].strip())
