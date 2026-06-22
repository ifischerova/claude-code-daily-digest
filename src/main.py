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
    try:
        update_readme(
            README_PATH, today, release.version, digest.subject, digest.body_markdown
        )
    except Exception as exc:  # noqa: BLE001
        print(f"README update failed ({exc}); archive saved, continuing.")
        exit_code = 1
    print(f"Archived digest for v{release.version}.")
    return exit_code


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
