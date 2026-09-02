"""Entry point: fetch -> check new -> summarize -> email -> archive."""
from __future__ import annotations

import datetime
import sys
import argparse
from pathlib import Path
from zoneinfo import ZoneInfo

from src.changelog import fetch_changelog, parse_latest
from src.config import load_config
from src.digest import digest_exists, update_readme, write_archive
from src.mailer import send_email
from src.summarizer import Digest, summarize

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "digests"
README_PATH = REPO_ROOT / "README.md"
_PRAGUE = ZoneInfo("Europe/Prague")


def run_test_email() -> int:
    """Send a manual, archive-free bilingual email to verify delivery."""
    config = load_config()
    digest = Digest(
        czech_subject="Zkušební e-mail denního přehledu Claude Code",
        czech_body_markdown=(
            "Toto je zkušební e-mail pro ověření doručení a českého formátu.\n\n"
            "**Co ověřuje** — Čeština je první a angličtina následuje níže."
        ),
        english_subject="Claude Code daily digest test email",
        english_body_markdown=(
            "This is a test email to verify delivery and the bilingual format.\n\n"
            "**What it checks** — Czech comes first and English follows below."
        ),
    )
    try:
        send_email(
            digest.subject,
            digest.body_markdown,
            api_key=config.resend_api_key,
            mail_from=config.mail_from,
            mail_to=config.mail_to,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Test email failed ({exc}).")
        return 1
    print("Test email sent; no digest was archived.")
    return 0


def _today() -> str:
    # Use Prague local date so the digest label matches the reader's day,
    # not the CI runner's UTC clock (which can be a day behind near midnight).
    return datetime.datetime.now(_PRAGUE).date().isoformat()


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
            czech_subject=f"Claude Code v{release.version}: poznámky k vydání",
            czech_body_markdown=(
                "_České shrnutí se nepodařilo vytvořit; níže jsou původní "
                "poznámky k vydání v angličtině._"
            ),
            english_subject=f"Claude Code v{release.version} released",
            english_body_markdown=(
                "_AI summary unavailable - here are the raw notes:_\n\n"
                + release.notes
            ),
        )

    # Send first. The committed archive is our "already sent" marker
    # (digest_exists checks it), so we only archive AFTER a successful send.
    # A failed send leaves no archive, so the next run retries instead of
    # silently dropping the email.
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
        print(f"Email failed ({exc}); not archiving so the next run retries.")
        return 1

    exit_code = 0
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test-email",
        action="store_true",
        help="send a bilingual test email without fetching or archiving a release",
    )
    args = parser.parse_args()
    sys.exit(run_test_email() if args.test_email else run())


if __name__ == "__main__":
    main()
