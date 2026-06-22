import pytest
import requests

from src.http_utils import raise_for_status_verbose


def test_raise_for_status_verbose_passes_on_ok():
    class FakeResp:
        def raise_for_status(self):
            pass

    raise_for_status_verbose(FakeResp())  # no exception


def test_raise_for_status_verbose_includes_body():
    class FakeResp:
        text = '{"error": "bad request detail"}'

        def raise_for_status(self):
            raise requests.HTTPError("400 Client Error")

    with pytest.raises(requests.HTTPError, match="bad request detail"):
        raise_for_status_verbose(FakeResp())
