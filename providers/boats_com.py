from __future__ import annotations

from typing import Any

from core.models import Boat, SearchCriteria
from .base_provider import Provider


class BoatsComProvider(Provider):
    """Provider placeholder for Boats.com results."""

    name = "Boats.com"

    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        return []
