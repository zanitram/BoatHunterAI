from __future__ import annotations

from typing import Any

from core.models import Boat, SearchCriteria
from .base_provider import Provider


class CraigslistProvider(Provider):
    """Provider placeholder for Craigslist results."""

    name = "Craigslist"

    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        return []
