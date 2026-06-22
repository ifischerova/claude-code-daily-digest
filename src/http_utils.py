"""Shared HTTP helpers."""
from __future__ import annotations

import requests


def raise_for_status_verbose(response) -> None:
    """Like response.raise_for_status(), but include the response body.

    The provider's JSON error detail (the useful part of a 4xx/5xx) is
    otherwise dropped by the default raise_for_status message.
    """
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        try:
            detail = response.text[:1000]
        except Exception:  # noqa: BLE001
            detail = "<unavailable>"
        raise requests.HTTPError(f"{exc}\nResponse body: {detail}") from exc
