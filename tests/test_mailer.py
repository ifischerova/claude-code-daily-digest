from src.mailer import render_html, send_email


def test_render_html_converts_markdown():
    html = render_html("# Hi\n\n- one\n- two")
    assert "<h1>" in html
    assert "<li>" in html


def test_send_email_posts_to_resend():
    class FakeResp:
        def raise_for_status(self):
            pass

    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["url"] = url
        captured["payload"] = json
        captured["auth"] = headers["Authorization"]
        return FakeResp()

    send_email(
        "Subj",
        "**hi**",
        api_key="k",
        mail_from="a@b.c",
        mail_to="d@e.f",
        http_post=fake_post,
    )
    assert captured["url"] == "https://api.resend.com/emails"
    assert captured["auth"] == "Bearer k"
    assert captured["payload"]["from"] == "a@b.c"
    assert captured["payload"]["to"] == ["d@e.f"]
    assert captured["payload"]["subject"] == "Subj"
    assert "<strong>" in captured["payload"]["html"]
    assert captured["payload"]["text"] == "**hi**"
