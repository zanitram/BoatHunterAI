from __future__ import annotations

import logging
import time
from typing import Optional

import requests


logger = logging.getLogger(__name__)


class HttpClient:
    """Reusable HTTP client for provider integrations.

    The client is intentionally stateless and reusable. It uses a single
    requests.Session internally so future provider integrations can share one
    networking layer with retry, logging, and extension hooks.
    """

    def __init__(self, timeout: int = 10, max_retries: int = 3) -> None:
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            }
        )

    def get(self, url: str) -> str:
        last_error: Optional[Exception] = None
        response: Optional[requests.Response] = None
        for attempt in range(1, self.max_retries + 1):
            started_at = time.perf_counter()
            try:
                logger.info("GET %s (attempt %s/%s)", url, attempt, self.max_retries)
                response = self.session.get(url, timeout=self.timeout)
                elapsed = time.perf_counter() - started_at
                logger.info(
                    "GET %s completed with status %s in %.3fs",
                    url,
                    response.status_code,
                    elapsed,
                )

                if response.status_code in {400, 401, 403, 404}:
                    raise requests.HTTPError(f"HTTP {response.status_code}")

                if response.status_code in {500, 502, 503, 504} and attempt < self.max_retries:
                    logger.warning(
                        "Transient HTTP failure for %s: %s (retry %s/%s)",
                        url,
                        response.status_code,
                        attempt,
                        self.max_retries,
                    )
                    continue

                response.raise_for_status()
                return response.text
            except requests.Timeout as exc:
                last_error = exc
                if attempt < self.max_retries:
                    logger.warning("Timeout for %s (retry %s/%s)", url, attempt, self.max_retries)
                    continue
                logger.error("Final timeout failure for %s: %s", url, exc)
                raise
            except requests.ConnectionError as exc:
                last_error = exc
                if attempt < self.max_retries:
                    logger.warning("Connection failure for %s (retry %s/%s)", url, attempt, self.max_retries)
                    continue
                logger.error("Final connection failure for %s: %s", url, exc)
                raise
            except requests.HTTPError as exc:
                if response is not None and response.status_code in {400, 401, 403, 404}:
                    logger.error("Non-retryable HTTP failure for %s: %s", url, exc)
                    raise
                last_error = exc
                if attempt < self.max_retries:
                    logger.warning("Transient HTTP failure for %s (retry %s/%s)", url, attempt, self.max_retries)
                    continue
                logger.error("Final HTTP failure for %s: %s", url, exc)
                raise
            except requests.RequestException as exc:
                last_error = exc
                if attempt < self.max_retries:
                    logger.warning("Request exception for %s (retry %s/%s)", url, attempt, self.max_retries)
                    continue
                logger.error("Final request failure for %s: %s", url, exc)
                raise

        if last_error is not None:
            raise last_error
        raise RuntimeError(f"Failed to fetch {url}")
