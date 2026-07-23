from __future__ import annotations

from typing import Any

from core.models import Boat, SearchCriteria
from .base_provider import Provider


class CastanetProvider(Provider):
    """Provider placeholder for Castanet results."""

    name = "Castanet"

    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        return []
