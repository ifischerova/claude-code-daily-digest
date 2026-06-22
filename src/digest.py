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
