from __future__ import annotations

from core.models import Boat
from core.search_request import SearchRequest
from .base_provider import Provider


class UsedCaProvider(Provider):
    """Provider placeholder for Used.ca results."""

    name = "Used.ca"

    def search(self, request: SearchRequest | None = None) -> list[Boat]:
        return []
