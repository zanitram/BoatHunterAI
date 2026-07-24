from __future__ import annotations

from abc import ABC, abstractmethod

from core.models import Boat
from core.search_request import SearchRequest


class Provider(ABC):
    """Shared interface for all boat providers."""

    name: str = "Provider"

    @abstractmethod
    def search(self, request: SearchRequest | None = None) -> list[Boat]:
        """Return a list of Boat objects for the supplied search criteria."""
        raise NotImplementedError
