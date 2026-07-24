from __future__ import annotations

from core.models import Boat
from core.search_request import SearchRequest
from .base_provider import Provider


class CastanetProvider(Provider):
    """Provider placeholder for Castanet results."""

    name = "Castanet"

    def search(self, request: SearchRequest | None = None) -> list[Boat]:
        return []
