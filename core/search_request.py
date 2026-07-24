from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from core.models import SearchCriteria


@dataclass
class SearchRequest:
    keywords: str = ""
    budget_min: int = 0
    budget_max: Optional[int] = None
    max_distance_km: Optional[int] = None
    length_min: Optional[float] = None
    length_max: Optional[float] = None
    brands: str = ""
    engine_preferences: str = ""
    freshwater_only: bool = False
    trailer_required: bool = False

    @classmethod
    def from_profile(cls, profile: SearchCriteria | None) -> "SearchRequest":
        if profile is None:
            return cls()

        return cls(
            keywords="",
            budget_min=profile.budget_min,
            budget_max=profile.budget_max,
            max_distance_km=profile.max_distance_km,
            length_min=profile.length_min,
            length_max=profile.length_max,
            brands=profile.brands,
            engine_preferences=profile.engine_preferences,
            freshwater_only=profile.freshwater_only,
            trailer_required=profile.trailer_required,
        )
