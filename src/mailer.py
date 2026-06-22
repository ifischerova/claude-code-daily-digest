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
