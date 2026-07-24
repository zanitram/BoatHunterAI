from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
import requests

from services.http_client import HttpClient


class TestHttpClient:
    def test_get_returns_text_on_success(self) -> None:
        client = HttpClient(timeout=5, max_retries=2)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "ok"
        mock_response.raise_for_status.return_value = None

        with patch.object(client.session, "get", return_value=mock_response) as get_mock:
            assert client.get("https://example.com") == "ok"

        assert get_mock.call_count == 1

    def test_get_raises_on_timeout(self) -> None:
        client = HttpClient(timeout=1, max_retries=2)

        with patch.object(client.session, "get", side_effect=requests.Timeout("boom")) as get_mock:
            with pytest.raises(requests.Timeout):
                client.get("https://example.com")

        assert get_mock.call_count == 2

    def test_get_retries_after_transient_timeout_and_succeeds(self) -> None:
        client = HttpClient(timeout=1, max_retries=3)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "retried"
        mock_response.raise_for_status.return_value = None

        with patch.object(
            client.session,
            "get",
            side_effect=[requests.Timeout("boom"), mock_response],
        ) as get_mock:
            assert client.get("https://example.com") == "retried"

        assert get_mock.call_count == 2

    def test_get_raises_after_exhausting_retries(self) -> None:
        client = HttpClient(timeout=1, max_retries=3)

        with patch.object(client.session, "get", side_effect=requests.ConnectionError("bad")) as get_mock:
            with pytest.raises(requests.ConnectionError):
                client.get("https://example.com")

        assert get_mock.call_count == 3

    def test_get_does_not_retry_on_not_found(self) -> None:
        client = HttpClient(timeout=1, max_retries=3)
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP 404")

        with patch.object(client.session, "get", return_value=mock_response) as get_mock:
            with pytest.raises(requests.HTTPError):
                client.get("https://example.com")

        assert get_mock.call_count == 1

    def test_get_retries_on_server_error(self) -> None:
        client = HttpClient(timeout=1, max_retries=2)
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "server"
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP 500")

        with patch.object(
            client.session,
            "get",
            side_effect=[mock_response, mock_response],
        ) as get_mock:
            with pytest.raises(requests.HTTPError):
                client.get("https://example.com")

        assert get_mock.call_count == 2
