from __future__ import annotations

from core.models import Boat
from core.search_request import SearchRequest
from .base_provider import Provider


class BoatsComProvider(Provider):
    """Provider placeholder for Boats.com results."""

    name = "Boats.com"

    def search(self, request: SearchRequest | None = None) -> list[Boat]:
        return []
