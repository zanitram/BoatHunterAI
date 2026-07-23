from __future__ import annotations

from typing import Any

from core.models import Boat, SearchCriteria
from .base_provider import Provider


class UsedCaProvider(Provider):
    """Provider placeholder for Used.ca results."""

    name = "Used.ca"

    def search(self, criteria: SearchCriteria | None = None) -> list[Boat]:
        return []
