from __future__ import annotations

from typing import Any

from core.models import Boat
from .base_provider import Provider


class CraigslistProvider(Provider):
    """Provider placeholder for Craigslist results."""

    name = "Craigslist"

    def search(self, criteria: dict[str, Any] | None = None) -> list[Boat]:
        return []
