import pytest

from src.summarizer import Digest, _parse_response, summarize


def test_parse_response_extracts_json_from_fenced_text():
    content = 'Sure!\n```json\n{"subject": "Hi 👋", "body": "## TL;DR\\nx"}\n```'
    digest = _parse_response(content)
    assert isinstance(digest, Digest)
    assert digest.subject == "Hi 👋"
    assert "TL;DR" in digest.body_markdown


def test_parse_response_raises_on_no_json():
    with pytest.raises(ValueError, match="No JSON object found"):
        _parse_response("This response has no JSON at all.")


def test_parse_response_raises_on_missing_keys():
    with pytest.raises(ValueError, match="missing subject/body"):
        _parse_response('{"title": "wrong key"}')


def test_parse_response_raises_on_malformed_json():
    with pytest.raises(ValueError, match="Malformed JSON"):
        _parse_response("here it is: {not valid json")


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
