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
