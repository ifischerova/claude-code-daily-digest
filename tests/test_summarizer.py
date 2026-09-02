import pytest

from src.summarizer import Digest, _parse_response, summarize


def test_parse_response_extracts_json_from_fenced_text():
    content = (
        'Sure!\n```json\n{"czech_subject": "Ahoj", '
        '"czech_body": "## Shrnutí\\nx", "english_subject": "Hi", '
        '"english_body": "## TL;DR\\nx"}\n```'
    )
    digest = _parse_response(content)
    assert isinstance(digest, Digest)
    assert digest.czech_subject == "Ahoj"
    assert digest.english_subject == "Hi"
    assert "TL;DR" in digest.body_markdown


def test_parse_response_raises_on_no_json():
    with pytest.raises(ValueError, match="No JSON object found"):
        _parse_response("This response has no JSON at all.")


def test_parse_response_raises_on_missing_keys():
    with pytest.raises(ValueError, match="missing bilingual digest fields"):
        _parse_response('{"title": "wrong key"}')


def test_parse_response_raises_on_malformed_json():
    with pytest.raises(ValueError, match="Malformed JSON"):
        _parse_response("here it is: {not valid json")


def test_summarize_raises_clearly_on_unexpected_response():
    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {"error": {"message": "rate limited"}}

    def fake_post(url, headers, json, timeout):
        return FakeResp()

    with pytest.raises(ValueError, match="Unexpected OpenRouter response"):
        summarize("1.0.0", "notes", api_key="k", model="m", http_post=fake_post)


def test_summarize_posts_to_openrouter_and_parses():
    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "choices": [
                    {
                        "message": {
                            "content": (
                                '{"czech_subject": "CS", "czech_body": "CB", '
                                '"english_subject": "EN", "english_body": "EB"}'
                            )
                        }
                    }
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
    assert digest.subject == "CS | EN"
    assert digest.body_markdown.index("CS") < digest.body_markdown.index("EN")
    assert captured["model"] == "m"
    assert captured["auth"] == "Bearer k"
    assert "openrouter.ai" in captured["url"]
