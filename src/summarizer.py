"""Turn raw changelog notes into a friendly newsletter via OpenRouter."""
from __future__ import annotations

import json
from dataclasses import dataclass

import requests

from src.http_utils import raise_for_status_verbose

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """You are the editor of a warm, friendly developer newsletter \
about Claude Code. Rewrite raw release notes so a busy human enjoys reading them.

Return ONLY a single JSON object, no prose around it:
{"czech_subject": "...", "czech_body": "...", "english_subject": "...", "english_body": "..."}

- Write the Czech fields in natural Czech and the English fields in natural English.
- Each "subject" is a concise, descriptive release headline with exactly one
  tasteful emoji. Do not write it in all capitals.
- Each "body" is Markdown with these sections, in this order:
  **TL;DR** — one sentence.
  **⭐ Highlight of the release** — the single most exciting change.
  **What's new** — plain-language bullets; translate jargon into human terms.
  **Why you'll care** — a short "so what".
  A warm one-line sign-off.

Keep both versions concise, equivalent in meaning, and human. Localize the
section headings naturally for their language. Do not invent features that are
not in the notes."""


@dataclass(frozen=True)
class Digest:
    czech_subject: str
    czech_body_markdown: str
    english_subject: str
    english_body_markdown: str

    @property
    def subject(self) -> str:
        return f"{self.czech_subject} | {self.english_subject}"

    @property
    def body_markdown(self) -> str:
        return (
            f"## {self.czech_subject}\n\n{self.czech_body_markdown}\n\n"
            f"---\n\n## {self.english_subject}\n\n{self.english_body_markdown}"
        )


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
        return Digest(
            czech_subject=data["czech_subject"],
            czech_body_markdown=data["czech_body"],
            english_subject=data["english_subject"],
            english_body_markdown=data["english_body"],
        )
    except (KeyError, TypeError) as exc:
        raise ValueError("Model response missing bilingual digest fields") from exc


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
    raise_for_status_verbose(response)
    data = response.json()
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        detail = data.get("error", data) if isinstance(data, dict) else data
        raise ValueError(f"Unexpected OpenRouter response: {detail}") from exc
    return _parse_response(content)
