from dataclasses import dataclass
from typing import Optional


@dataclass
class Boat:
    name: str
    price: int
    location: str
    engine: str
    length: float
    trailer: bool
    score: int = 0
    notes: str = ""
    id: Optional[int] = None
    source: str = "manual"

    @classmethod
    def from_row(cls, row):
        if not row:
            return None

        boat_id, name, price, location, engine, length, trailer, score, notes = row
        return cls(
            name=name,
            price=price,
            location=location,
            engine=engine,
            length=length,
            trailer=bool(trailer),
            score=score,
            notes=notes,
            id=boat_id,
        )


@dataclass
class SearchCriteria:
    name: str = "Default profile"
    budget_min: int = 0
    budget_max: Optional[int] = None
    max_distance_km: Optional[int] = None
    length_min: Optional[float] = None
    length_max: Optional[float] = None
    brands: str = ""
    engine_preferences: str = ""
    freshwater_only: bool = False
    trailer_required: bool = False
    id: Optional[int] = None

    @classmethod
    def from_row(cls, row):
        if not row:
            return None

        (
            profile_id,
            name,
            budget_min,
            budget_max,
            max_distance_km,
            length_min,
            length_max,
            brands,
            engine_preferences,
            freshwater_only,
            trailer_required,
        ) = row

        return cls(
            name=name,
            budget_min=budget_min or 0,
            budget_max=budget_max,
            max_distance_km=max_distance_km,
            length_min=length_min,
            length_max=length_max,
            brands=brands or "",
            engine_preferences=engine_preferences or "",
            freshwater_only=bool(freshwater_only),
            trailer_required=bool(trailer_required),
            id=profile_id,
        )

    def to_db_tuple(self):
        return (
            self.name,
            self.budget_min,
            self.budget_max,
            self.max_distance_km,
            self.length_min,
            self.length_max,
            self.brands,
            self.engine_preferences,
            int(self.freshwater_only),
            int(self.trailer_required),
        )