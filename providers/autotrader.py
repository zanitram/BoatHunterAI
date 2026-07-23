from __future__ import annotations

from typing import Any

from core.models import Boat
from .base_provider import Provider


class AutoTraderProvider(Provider):
    """Provider placeholder for AutoTrader results."""

    name = "AutoTrader"

    def search(self, criteria: dict[str, Any] | None = None) -> list[Boat]:
        return []
