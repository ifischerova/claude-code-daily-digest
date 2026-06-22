import pytest

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


def test_update_readme_raises_when_marker_missing(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("no markers here\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing one or both"):
        update_readme(readme, "2026-06-22", "1.2.0", "Subj", "body")
