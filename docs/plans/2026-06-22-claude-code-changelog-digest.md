# Claude Code Changelog Digest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A scheduled GitHub Action that fetches the latest Claude Code changelog, has an LLM rewrite it as a friendly newsletter, emails it via Resend, and commits the digest into the repo as a public archive.

**Architecture:** Small, focused Python modules (`changelog`, `summarizer`, `mailer`, `digest`, `config`, `main`). All network calls are injected so they can be tested without live APIs. A GitHub Actions workflow runs `python -m src.main` daily and commits any new digest.

**Tech Stack:** Python 3.12, `requests`, `markdown`, `pytest`, GitHub Actions, OpenRouter API (OpenAI-compatible), Resend email API.

## Global Constraints

- Python 3.12. Standard library + `requests` + `markdown` only at runtime; `pytest` for tests.
- No secret is ever written to a tracked file. Secrets are read from environment variables, supplied by GitHub Actions secrets.
- Every network boundary (HTTP get/post) is an injectable parameter (`http_get` / `http_post`) defaulting to `requests`, so units test without the network.
- Default model slug: `google/gemini-3.1-flash-lite` (overridable via `OPENROUTER_MODEL`). Default sender: `onboarding@resend.dev` (overridable via `MAIL_FROM`).
- Commit author for automated digest commits: `Iva Fischerova <fischerova.ivka@gmail.com>`.
- Digest voice: friendly newsletter editor — TL;DR, ⭐ Highlight, What's new (plain language), Why you'll care, warm sign-off.
- Tests run from the repo root via `pytest` (config sets `pythonpath = .`).

---

### Task 1: Project scaffolding & tooling

**Files:**
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `requirements-dev.txt`
- Create: `pytest.ini`
- Create: `src/__init__.py`
- Create: `digests/.gitkeep`
- Create: `tests/test_smoke.py`

**Interfaces:**
- Consumes: nothing.
- Produces: a runnable `pytest` harness and the `src` package other tasks import from.

- [ ] **Step 1: Initialize git**

```bash
cd "C:/Users/iva.fischerova/OneDrive - Direct/Plocha/soukrome/claude-news"
git init
git config user.name "Iva Fischerova"
git config user.email "fischerova.ivka@gmail.com"
```

- [ ] **Step 2: Create `.gitignore`**

```gitignore
__pycache__/
*.pyc
.env
.venv/
.pytest_cache/
```

- [ ] **Step 3: Create `requirements.txt`**

```
requests>=2.31
markdown>=3.5
```

- [ ] **Step 4: Create `requirements-dev.txt`**

```
-r requirements.txt
pytest>=8.0
```

- [ ] **Step 5: Create `pytest.ini`**

```ini
[pytest]
pythonpath = .
testpaths = tests
```

- [ ] **Step 6: Create `src/__init__.py`** (empty file)

```python
```

- [ ] **Step 7: Create `digests/.gitkeep`** (empty file — keeps the dir in git)

```text
```

- [ ] **Step 8: Write the smoke test** in `tests/test_smoke.py`

```python
def test_src_package_importable():
    import src  # noqa: F401
```

- [ ] **Step 9: Install dev deps and run the smoke test**

Run:
```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
Expected: 1 passed.

- [ ] **Step 10: Commit**

```bash
git add .gitignore requirements.txt requirements-dev.txt pytest.ini src/__init__.py digests/.gitkeep tests/test_smoke.py
git commit -m "chore: scaffold project and test harness"
```

---

### Task 2: Changelog fetch & parse

**Files:**
- Create: `src/changelog.py`
- Test: `tests/test_changelog.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `DEFAULT_URL: str`
  - `@dataclass(frozen=True) Release(version: str, notes: str)`
  - `fetch_changelog(url: str = DEFAULT_URL, *, http_get=requests.get) -> str`
  - `parse_latest(text: str) -> Release` (raises `ValueError` if no version heading)

- [ ] **Step 1: Write the failing tests** in `tests/test_changelog.py`

```python
import pytest

from src.changelog import Release, fetch_changelog, parse_latest

SAMPLE = """# Changelog

## 1.2.0

- Added checkpoints
- Fixed a crash

## 1.1.0

- Older stuff
"""


def test_parse_latest_returns_newest_version():
    release = parse_latest(SAMPLE)
    assert isinstance(release, Release)
    assert release.version == "1.2.0"
    assert "checkpoints" in release.notes
    assert "Older stuff" not in release.notes


def test_parse_latest_single_version():
    text = "# Changelog\n\n## 0.1.0\n\n- First\n"
    assert parse_latest(text).version == "0.1.0"


def test_parse_latest_no_version_raises():
    with pytest.raises(ValueError):
        parse_latest("# Changelog\n\nNo versions here\n")


def test_fetch_changelog_uses_injected_getter():
    class FakeResp:
        text = "hello"

        def raise_for_status(self):
            pass

    captured = {}

    def fake_get(url, timeout):
        captured["url"] = url
        return FakeResp()

    assert fetch_changelog(http_get=fake_get) == "hello"
    assert "CHANGELOG.md" in captured["url"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_changelog.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.changelog'`.

- [ ] **Step 3: Write the implementation** in `src/changelog.py`

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_changelog.py -q`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add src/changelog.py tests/test_changelog.py
git commit -m "feat: fetch and parse latest changelog release"
```

---

### Task 3: Summarizer (OpenRouter)

**Files:**
- Create: `src/summarizer.py`
- Test: `tests/test_summarizer.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `@dataclass(frozen=True) Digest(subject: str, body_markdown: str)`
  - `summarize(version: str, notes: str, *, api_key: str, model: str, http_post=requests.post) -> Digest`
  - `_parse_response(content: str) -> Digest` (extracts the first JSON object from model output)

- [ ] **Step 1: Write the failing tests** in `tests/test_summarizer.py`

```python
from src.summarizer import Digest, _parse_response, summarize


def test_parse_response_extracts_json_from_fenced_text():
    content = 'Sure!\n```json\n{"subject": "Hi 👋", "body": "## TL;DR\\nx"}\n```'
    digest = _parse_response(content)
    assert isinstance(digest, Digest)
    assert digest.subject == "Hi 👋"
    assert "TL;DR" in digest.body_markdown


def test_summarize_posts_to_openrouter_and_parses():
    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "choices": [
                    {"message": {"content": '{"subject": "S", "body": "B"}'}}
                ]
            }

    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["url"] = url
        captured["model"] = json["model"]
        captured["auth"] = headers["Authorization"]
        return FakeResp()

    digest = summarize(
        "1.0.0", "notes", api_key="k", model="m", http_post=fake_post
    )
    assert digest.subject == "S"
    assert digest.body_markdown == "B"
    assert captured["model"] == "m"
    assert captured["auth"] == "Bearer k"
    assert "openrouter.ai" in captured["url"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_summarizer.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.summarizer'`.

- [ ] **Step 3: Write the implementation** in `src/summarizer.py`

```python
"""Turn raw changelog notes into a friendly newsletter via OpenRouter."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass

import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)

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
    match = _JSON_RE.search(content)
    if not match:
        raise ValueError("No JSON object found in model response")
    data = json.loads(match.group(0))
    return Digest(subject=data["subject"], body_markdown=data["body"])


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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_summarizer.py -q`
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add src/summarizer.py tests/test_summarizer.py
git commit -m "feat: summarize release notes via OpenRouter"
```

---

### Task 4: Mailer (Resend)

**Files:**
- Create: `src/mailer.py`
- Test: `tests/test_mailer.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `render_html(body_markdown: str) -> str`
  - `send_email(subject: str, body_markdown: str, *, api_key: str, mail_from: str, mail_to: str, http_post=requests.post) -> None`

- [ ] **Step 1: Write the failing tests** in `tests/test_mailer.py`

```python
from src.mailer import render_html, send_email


def test_render_html_converts_markdown():
    html = render_html("# Hi\n\n- one\n- two")
    assert "<h1>" in html
    assert "<li>" in html


def test_send_email_posts_to_resend():
    class FakeResp:
        def raise_for_status(self):
            pass

    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["url"] = url
        captured["payload"] = json
        captured["auth"] = headers["Authorization"]
        return FakeResp()

    send_email(
        "Subj",
        "**hi**",
        api_key="k",
        mail_from="a@b.c",
        mail_to="d@e.f",
        http_post=fake_post,
    )
    assert captured["url"] == "https://api.resend.com/emails"
    assert captured["auth"] == "Bearer k"
    assert captured["payload"]["from"] == "a@b.c"
    assert captured["payload"]["to"] == ["d@e.f"]
    assert captured["payload"]["subject"] == "Subj"
    assert "<strong>" in captured["payload"]["html"]
    assert captured["payload"]["text"] == "**hi**"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_mailer.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.mailer'`.

- [ ] **Step 3: Write the implementation** in `src/mailer.py`

```python
"""Send the digest email via the Resend API."""
from __future__ import annotations

import markdown as md
import requests

RESEND_URL = "https://api.resend.com/emails"


def render_html(body_markdown: str) -> str:
    return md.markdown(body_markdown, extensions=["extra"])


def send_email(
    subject: str,
    body_markdown: str,
    *,
    api_key: str,
    mail_from: str,
    mail_to: str,
    http_post=requests.post,
) -> None:
    payload = {
        "from": mail_from,
        "to": [mail_to],
        "subject": subject,
        "html": render_html(body_markdown),
        "text": body_markdown,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = http_post(RESEND_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_mailer.py -q`
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add src/mailer.py tests/test_mailer.py
git commit -m "feat: send digest email via Resend"
```

---

### Task 5: Digest archive & README updater

**Files:**
- Create: `src/digest.py`
- Test: `tests/test_digest.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `LATEST_START: str` = `"<!-- LATEST:START -->"`, `LATEST_END: str` = `"<!-- LATEST:END -->"`
  - `archive_filename(date: str, version: str) -> str`
  - `digest_exists(version: str, digests_dir: Path) -> bool`
  - `write_archive(digests_dir: Path, date: str, version: str, subject: str, body_markdown: str) -> Path`
  - `update_readme(readme_path: Path, date: str, version: str, subject: str, body_markdown: str) -> None`

- [ ] **Step 1: Write the failing tests** in `tests/test_digest.py`

```python
from src.digest import (
    LATEST_END,
    LATEST_START,
    archive_filename,
    digest_exists,
    update_readme,
    write_archive,
)


def test_archive_filename_format():
    assert archive_filename("2026-06-22", "1.2.0") == "2026-06-22-v1.2.0.md"


def test_digest_exists_detects_version(tmp_path):
    (tmp_path / "2026-01-01-v1.0.0.md").write_text("x", encoding="utf-8")
    assert digest_exists("1.0.0", tmp_path)
    assert not digest_exists("2.0.0", tmp_path)


def test_write_archive_creates_file(tmp_path):
    path = write_archive(tmp_path, "2026-06-22", "1.2.0", "Subj 🎉", "**body**")
    assert path.exists()
    content = path.read_text(encoding="utf-8")
    assert "Subj 🎉" in content
    assert "1.2.0" in content
    assert "**body**" in content


def test_update_readme_replaces_only_the_block(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        f"Top\n{LATEST_START}\nold\n{LATEST_END}\nBottom\n", encoding="utf-8"
    )
    update_readme(readme, "2026-06-22", "1.2.0", "New Subj", "new body")
    text = readme.read_text(encoding="utf-8")
    assert "old" not in text
    assert "New Subj" in text
    assert "Top" in text and "Bottom" in text
    assert text.count(LATEST_START) == 1
    assert text.count(LATEST_END) == 1
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_digest.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.digest'`.

- [ ] **Step 3: Write the implementation** in `src/digest.py`

```python
"""Write digest archives and update the README showcase block."""
from __future__ import annotations

from pathlib import Path

LATEST_START = "<!-- LATEST:START -->"
LATEST_END = "<!-- LATEST:END -->"


def archive_filename(date: str, version: str) -> str:
    return f"{date}-v{version}.md"


def digest_exists(version: str, digests_dir: Path) -> bool:
    return any(digests_dir.glob(f"*-v{version}.md"))


def write_archive(
    digests_dir: Path,
    date: str,
    version: str,
    subject: str,
    body_markdown: str,
) -> Path:
    digests_dir.mkdir(parents=True, exist_ok=True)
    path = digests_dir / archive_filename(date, version)
    content = (
        f"# {subject}\n\n_Claude Code v{version} — {date}_\n\n{body_markdown}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def update_readme(
    readme_path: Path,
    date: str,
    version: str,
    subject: str,
    body_markdown: str,
) -> None:
    text = readme_path.read_text(encoding="utf-8")
    block = (
        f"{LATEST_START}\n\n"
        f"### {subject}\n\n"
        f"_Claude Code v{version} — {date}_\n\n"
        f"{body_markdown}\n\n"
        f"{LATEST_END}"
    )
    before, _, rest = text.partition(LATEST_START)
    _, _, after = rest.partition(LATEST_END)
    readme_path.write_text(before + block + after, encoding="utf-8")
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_digest.py -q`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add src/digest.py tests/test_digest.py
git commit -m "feat: archive digests and update README showcase"
```

---

### Task 6: Config & orchestration

**Files:**
- Create: `src/config.py`
- Create: `src/main.py`
- Test: `tests/test_config.py`
- Test: `tests/test_main.py`

**Interfaces:**
- Consumes: `fetch_changelog`, `parse_latest`, `Release` (Task 2); `summarize`, `Digest` (Task 3); `send_email` (Task 4); `digest_exists`, `write_archive`, `update_readme` (Task 5).
- Produces:
  - `@dataclass(frozen=True) Config(openrouter_api_key, openrouter_model, resend_api_key, mail_from, mail_to)` (all `str`)
  - `load_config(env=os.environ) -> Config`
  - `run(*, today: str | None = None) -> int` (orchestrator; returns process exit code)
  - `main() -> None` (calls `sys.exit(run())`)

- [ ] **Step 1: Write the failing tests** in `tests/test_config.py`

```python
import pytest

from src.config import Config, load_config


def test_load_config_reads_required_and_defaults():
    env = {
        "OPENROUTER_API_KEY": "ok",
        "RESEND_API_KEY": "rk",
        "MAIL_TO": "me@example.com",
    }
    config = load_config(env)
    assert isinstance(config, Config)
    assert config.openrouter_api_key == "ok"
    assert config.resend_api_key == "rk"
    assert config.mail_to == "me@example.com"
    assert config.openrouter_model == "google/gemini-3.1-flash-lite"
    assert config.mail_from == "onboarding@resend.dev"


def test_load_config_honours_overrides():
    env = {
        "OPENROUTER_API_KEY": "ok",
        "OPENROUTER_MODEL": "qwen/qwen3.6-flash",
        "RESEND_API_KEY": "rk",
        "MAIL_FROM": "news@my.dev",
        "MAIL_TO": "me@example.com",
    }
    config = load_config(env)
    assert config.openrouter_model == "qwen/qwen3.6-flash"
    assert config.mail_from == "news@my.dev"


def test_load_config_missing_required_raises():
    with pytest.raises(KeyError):
        load_config({})
```

- [ ] **Step 2: Run config tests to verify they fail**

Run: `python -m pytest tests/test_config.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.config'`.

- [ ] **Step 3: Write `src/config.py`**

```python
"""Runtime configuration from environment variables."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    openrouter_api_key: str
    openrouter_model: str
    resend_api_key: str
    mail_from: str
    mail_to: str


def load_config(env=os.environ) -> Config:
    return Config(
        openrouter_api_key=env["OPENROUTER_API_KEY"],
        openrouter_model=env.get(
            "OPENROUTER_MODEL", "google/gemini-3.1-flash-lite"
        ),
        resend_api_key=env["RESEND_API_KEY"],
        mail_from=env.get("MAIL_FROM", "onboarding@resend.dev"),
        mail_to=env["MAIL_TO"],
    )
```

- [ ] **Step 4: Run config tests to verify they pass**

Run: `python -m pytest tests/test_config.py -q`
Expected: 3 passed.

- [ ] **Step 5: Write the failing tests** in `tests/test_main.py`

```python
from types import SimpleNamespace

import src.main as m
from src.changelog import Release
from src.summarizer import Digest

FAKE_CONFIG = SimpleNamespace(
    openrouter_api_key="k",
    openrouter_model="model",
    resend_api_key="rk",
    mail_from="a@b.c",
    mail_to="d@e.f",
)


def _readme_with_block(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "x\n<!-- LATEST:START -->\nold\n<!-- LATEST:END -->\ny\n",
        encoding="utf-8",
    )
    return readme


def test_run_happy_path_emails_and_archives(tmp_path, monkeypatch):
    digests = tmp_path / "digests"
    readme = _readme_with_block(tmp_path)
    monkeypatch.setattr(m, "DIGESTS_DIR", digests)
    monkeypatch.setattr(m, "README_PATH", readme)
    monkeypatch.setattr(m, "load_config", lambda: FAKE_CONFIG)
    monkeypatch.setattr(m, "fetch_changelog", lambda: "raw")
    monkeypatch.setattr(m, "parse_latest", lambda raw: Release("9.9.9", "notes"))
    monkeypatch.setattr(
        m, "summarize", lambda *a, **k: Digest("Subj 🎉", "body")
    )
    sent = {}
    monkeypatch.setattr(
        m, "send_email", lambda *a, **k: sent.update(ok=True)
    )

    code = m.run(today="2026-06-22")

    assert code == 0
    assert sent.get("ok") is True
    assert (digests / "2026-06-22-v9.9.9.md").exists()
    assert "Subj 🎉" in readme.read_text(encoding="utf-8")


def test_run_skips_when_version_already_digested(tmp_path, monkeypatch):
    digests = tmp_path / "digests"
    digests.mkdir()
    (digests / "2026-01-01-v9.9.9.md").write_text("x", encoding="utf-8")
    monkeypatch.setattr(m, "DIGESTS_DIR", digests)
    monkeypatch.setattr(m, "load_config", lambda: FAKE_CONFIG)
    monkeypatch.setattr(m, "fetch_changelog", lambda: "raw")
    monkeypatch.setattr(m, "parse_latest", lambda raw: Release("9.9.9", "notes"))
    called = {}
    monkeypatch.setattr(
        m, "summarize", lambda *a, **k: called.setdefault("summarize", True)
    )

    assert m.run() == 0
    assert "summarize" not in called


def test_run_archives_even_if_email_fails(tmp_path, monkeypatch):
    digests = tmp_path / "digests"
    readme = _readme_with_block(tmp_path)
    monkeypatch.setattr(m, "DIGESTS_DIR", digests)
    monkeypatch.setattr(m, "README_PATH", readme)
    monkeypatch.setattr(m, "load_config", lambda: FAKE_CONFIG)
    monkeypatch.setattr(m, "fetch_changelog", lambda: "raw")
    monkeypatch.setattr(m, "parse_latest", lambda raw: Release("9.9.9", "notes"))
    monkeypatch.setattr(
        m, "summarize", lambda *a, **k: Digest("Subj", "body")
    )

    def boom(*a, **k):
        raise RuntimeError("smtp down")

    monkeypatch.setattr(m, "send_email", boom)

    code = m.run(today="2026-06-22")

    assert code == 1
    assert (digests / "2026-06-22-v9.9.9.md").exists()


def test_run_falls_back_to_raw_notes_when_summary_fails(tmp_path, monkeypatch):
    digests = tmp_path / "digests"
    readme = _readme_with_block(tmp_path)
    monkeypatch.setattr(m, "DIGESTS_DIR", digests)
    monkeypatch.setattr(m, "README_PATH", readme)
    monkeypatch.setattr(m, "load_config", lambda: FAKE_CONFIG)
    monkeypatch.setattr(m, "fetch_changelog", lambda: "raw")
    monkeypatch.setattr(
        m, "parse_latest", lambda raw: Release("9.9.9", "RAWNOTE")
    )

    def boom(*a, **k):
        raise RuntimeError("model down")

    monkeypatch.setattr(m, "summarize", boom)
    monkeypatch.setattr(m, "send_email", lambda *a, **k: None)

    code = m.run(today="2026-06-22")

    assert code == 0
    archived = (digests / "2026-06-22-v9.9.9.md").read_text(encoding="utf-8")
    assert "RAWNOTE" in archived
```

- [ ] **Step 6: Run main tests to verify they fail**

Run: `python -m pytest tests/test_main.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.main'`.

- [ ] **Step 7: Write `src/main.py`**

```python
"""Entry point: fetch -> check new -> summarize -> email -> archive."""
from __future__ import annotations

import datetime
import sys
from pathlib import Path

from src.changelog import fetch_changelog, parse_latest
from src.config import load_config
from src.digest import digest_exists, update_readme, write_archive
from src.mailer import send_email
from src.summarizer import Digest, summarize

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "digests"
README_PATH = REPO_ROOT / "README.md"


def _today() -> str:
    return datetime.date.today().isoformat()


def run(*, today: str | None = None) -> int:
    config = load_config()
    today = today or _today()

    raw = fetch_changelog()
    release = parse_latest(raw)

    if digest_exists(release.version, DIGESTS_DIR):
        print(f"Nothing new - v{release.version} already digested.")
        return 0

    try:
        digest = summarize(
            release.version,
            release.notes,
            api_key=config.openrouter_api_key,
            model=config.openrouter_model,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"AI summary failed ({exc}); falling back to raw notes.")
        digest = Digest(
            subject=f"📝 Claude Code v{release.version} released",
            body_markdown=(
                "_AI summary unavailable - here are the raw notes:_\n\n"
                + release.notes
            ),
        )

    exit_code = 0
    try:
        send_email(
            digest.subject,
            digest.body_markdown,
            api_key=config.resend_api_key,
            mail_from=config.mail_from,
            mail_to=config.mail_to,
        )
        print("Email sent.")
    except Exception as exc:  # noqa: BLE001
        print(f"Email failed ({exc}); archiving anyway.")
        exit_code = 1

    write_archive(
        DIGESTS_DIR, today, release.version, digest.subject, digest.body_markdown
    )
    update_readme(
        README_PATH, today, release.version, digest.subject, digest.body_markdown
    )
    print(f"Archived digest for v{release.version}.")
    return exit_code


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
```

- [ ] **Step 8: Run the full test suite to verify everything passes**

Run: `python -m pytest -q`
Expected: all tests pass (smoke + changelog + summarizer + mailer + digest + config + main).

- [ ] **Step 9: Commit**

```bash
git add src/config.py src/main.py tests/test_config.py tests/test_main.py
git commit -m "feat: add config and orchestrator entry point"
```

---

### Task 7: Workflow, README & project docs

**Files:**
- Create: `.github/workflows/daily-digest.yml`
- Create: `README.md`
- Create: `.env.example`
- Create: `LICENSE`

**Interfaces:**
- Consumes: `python -m src.main` (Task 6); the `<!-- LATEST:START -->` / `<!-- LATEST:END -->` markers (Task 5).
- Produces: the scheduled automation and the public-facing showcase. (No unit tests — validated by a manual `workflow_dispatch` run after secrets are set.)

- [ ] **Step 1: Create `.github/workflows/daily-digest.yml`**

```yaml
name: Daily Claude Code Digest

on:
  schedule:
    - cron: "0 5 * * *"  # ~07:00 Europe/Prague (CEST)
  workflow_dispatch:

permissions:
  contents: write

jobs:
  digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: python -m pip install -r requirements.txt

      - name: Generate and send digest
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          OPENROUTER_MODEL: ${{ vars.OPENROUTER_MODEL || 'google/gemini-3.1-flash-lite' }}
          RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
          MAIL_FROM: ${{ vars.MAIL_FROM || 'onboarding@resend.dev' }}
          MAIL_TO: ${{ secrets.MAIL_TO }}
        run: python -m src.main

      - name: Commit new digest
        run: |
          git config user.name "Iva Fischerova"
          git config user.email "fischerova.ivka@gmail.com"
          git add digests README.md
          if git diff --staged --quiet; then
            echo "No changes to commit."
          else
            git commit -m "chore: daily digest $(date +%F)"
            git push
          fi
```

- [ ] **Step 2: Create `.env.example`**

```dotenv
# Copy to .env for local runs. NEVER commit a real .env.
OPENROUTER_API_KEY=sk-or-your-key-here
OPENROUTER_MODEL=google/gemini-3.1-flash-lite
RESEND_API_KEY=re_your-key-here
MAIL_FROM=onboarding@resend.dev
MAIL_TO=you@example.com
```

- [ ] **Step 3: Create `README.md`** (includes the LATEST markers so the first run can fill them)

```markdown
# 📰 Claude Code Daily Digest

> I got tired of reading changelogs, so I taught an AI to read them for me — and email me the good parts every morning.

This repo is a tiny, fully automated newsletter. Every day a GitHub Action checks the [Claude Code](https://github.com/anthropics/claude-code) changelog. When there's a new release, an LLM (via [OpenRouter](https://openrouter.ai)) rewrites the notes as a friendly digest, emails it to me through [Resend](https://resend.com), and commits it here as a permanent archive.

No servers. No cost beyond pennies of tokens. Just a robot doing my reading for me. ☕

## ✨ How it works

```
GitHub Action (daily cron)
  └─ fetch CHANGELOG.md from anthropics/claude-code
       └─ new version? ── no ─► stop quietly
              │ yes
              ▼
        LLM writes a friendly digest (OpenRouter)
              ▼
        email it (Resend)  +  commit it to /digests
```

## 📬 Latest digest

<!-- LATEST:START -->

_The first scheduled run will drop the latest digest here._

<!-- LATEST:END -->

Browse every past edition in [`/digests`](./digests).

## 🛠️ Run it yourself

1. Fork this repo.
2. Add **Actions secrets** (`Settings → Secrets and variables → Actions`):
   - `OPENROUTER_API_KEY` — from openrouter.ai
   - `RESEND_API_KEY` — from resend.com
   - `MAIL_TO` — where the digest is sent
3. (Optional) Add **Actions variables**: `OPENROUTER_MODEL`, `MAIL_FROM`.
4. Enable Actions, then run **Daily Claude Code Digest → Run workflow** to test.

Local run:

```bash
pip install -r requirements-dev.txt
cp .env.example .env   # fill in your keys
pytest
python -m src.main
```

## 🧱 Tech

Python · OpenRouter · Resend · GitHub Actions. Tested with `pytest`; every network call is injectable so the suite runs offline.

---

Built by Iva Fischerova.
```

- [ ] **Step 4: Create `LICENSE`** (MIT)

```text
MIT License

Copyright (c) 2026 Iva Fischerova

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 5: Verify the full suite still passes**

Run: `python -m pytest -q`
Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/daily-digest.yml README.md .env.example LICENSE
git commit -m "feat: add workflow, README showcase, and project docs"
```

---

## Post-implementation (manual, by Iva)

These steps need real credentials and a GitHub remote, so they're done by hand after the code is in:

1. **Rotate** the OpenRouter key that was shared in chat; create a fresh one.
2. Create the GitHub repo and `git push`.
3. Add the three secrets (`OPENROUTER_API_KEY`, `RESEND_API_KEY`, `MAIL_TO`).
4. Verify the exact OpenRouter model slug at <https://openrouter.ai/models> and set the `OPENROUTER_MODEL` variable if the default needs adjusting.
5. Trigger **Run workflow** once to confirm an email arrives and a digest file appears.

## Notes / open items

- The OpenRouter model slugs (`google/gemini-3.1-flash-lite`, `qwen/qwen3.6-flash`) should be confirmed against the live `/models` list; the code reads the slug from config so swapping is a one-line variable change.
- Confirm `anthropics/claude-code` default branch is `main` (used in the raw changelog URL). If it differs, update `DEFAULT_URL` in `src/changelog.py`.
```