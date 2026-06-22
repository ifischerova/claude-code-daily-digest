"""Turn raw changelog notes into a friendly newsletter via OpenRouter."""
from __future__ import annotations

import json
from dataclasses import dataclass

import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """You are the editor of a warm, friendly developer newsletter \
about Claude Code. Rewrite raw release notes so a busy human enjoys reading them.

Return ONLY a single JSON object, no prose around it:
{"subject": "...", "body": "..."}

- "subject": a catchy one-line subject with exactly one tasteful emoji.
- "body": Markdown with these sections, in this order:
  **TL;DR** — one sentence.
  **⭐ Highlight of the release** — the single most exciting change.
  **What's new** — plain-language bullets; translate jargon into human terms.
  **Why you'll care** — a short "so what".
  A warm one-line sign-off.

Keep it concise and human. Do not invent features that are not in the notes."""


@dataclass(frozen=True)
class Digest:
    subject: str
    body_markdown: str


def _build_messages(version: str, notes: str) -> list[dict]:
    user = (
        f"Claude Code {version} was just released. "
        f"Here are the raw release notes:\n\n{notes}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user},
    ]


def _parse_response(content: str) -> Digest:
    start = content.find("{")
    if start == -1:
        raise ValueError("No JSON object found in model response")
    try:
        data, _ = json.JSONDecoder().raw_decode(content[start:])
    except json.JSONDecodeError as exc:
        raise ValueError("Malformed JSON in model response") from exc
    try:
        return Digest(subject=data["subject"], body_markdown=data["body"])
    except (KeyError, TypeError) as exc:
        raise ValueError("Model response missing subject/body") from exc


def summarize(
    version: str,
    notes: str,
    *,
    api_key: str,
    model: str,
    http_post=requests.post,
) -> Digest:
    payload = {
        "model": model,
        "messages": _build_messages(version, notes),
        "temperature": 0.7,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = http_post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    return _parse_response(content)
