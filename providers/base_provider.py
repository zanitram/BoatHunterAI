from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.models import Boat


class Provider(ABC):
    name: str = "Provider"

    @abstractmethod
    def search(self, criteria: dict[str, Any] | None = None) -> list[Boat]:
        """Return a list of Boat objects for the given criteria."""
        raise NotImplementedError
