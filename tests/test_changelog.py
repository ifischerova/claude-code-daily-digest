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
