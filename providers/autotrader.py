from __future__ import annotations

from core.models import Boat
from core.search_request import SearchRequest
from .base_provider import Provider


class AutoTraderProvider(Provider):
    """Provider placeholder for AutoTrader results."""

    name = "AutoTrader"

    def search(self, request: SearchRequest | None = None) -> list[Boat]:
        return []
