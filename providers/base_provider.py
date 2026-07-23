from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.models import Boat, SearchCriteria


class Provider(ABC):
    """Shared interface for all boat providers."""

    name: str = "Provider"

    @abstractmethod
    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        """Return a list of Boat objects for the supplied search criteria."""
        raise NotImplementedError
