import pytest

from src.config import Config, load_config


def test_load_config_reads_required_and_defaults():
    env = {
        "OPENROUTER_API_KEY": "ok",
        "RESEND_API_KEY": "rk",
        "MAIL_TO": "me@example.com",
    }
    config = load_config(env)
    assert isinstance(config, Config)
    assert config.openrouter_api_key == "ok"
    assert config.resend_api_key == "rk"
    assert config.mail_to == "me@example.com"
    assert config.openrouter_model == "google/gemini-3.1-flash-lite"
    assert config.mail_from == "onboarding@resend.dev"


def test_load_config_honours_overrides():
    env = {
        "OPENROUTER_API_KEY": "ok",
        "OPENROUTER_MODEL": "qwen/qwen3.6-flash",
        "RESEND_API_KEY": "rk",
        "MAIL_FROM": "news@my.dev",
        "MAIL_TO": "me@example.com",
    }
    config = load_config(env)
    assert config.openrouter_model == "qwen/qwen3.6-flash"
    assert config.mail_from == "news@my.dev"


def test_load_config_missing_required_raises():
    with pytest.raises(KeyError):
        load_config({})
