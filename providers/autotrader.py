from __future__ import annotations

from typing import Any

from core.models import Boat, SearchCriteria
from .base_provider import Provider


class AutoTraderProvider(Provider):
    """Provider placeholder for AutoTrader results."""

    name = "AutoTrader"

    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        return []
