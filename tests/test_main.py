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
