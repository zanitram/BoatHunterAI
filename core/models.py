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