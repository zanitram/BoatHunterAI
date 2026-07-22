from core.models import Boat
from core.scoring import calculate_score


def test_calculate_score_prefers_common_engine_and_price():
    boat = Boat(
        name="Starcraft",
        price=8500,
        location="Montreal",
        engine="5.0 MPI",
        length=24,
        trailer=True,
        notes=""
    )
    assert calculate_score(boat) >= 90


def test_calculate_score_penalizes_big_block_engine():
    boat = Boat(
        name="Old boat",
        price=14000,
        location="Vancouver",
        engine="454 big block",
        length=22,
        trailer=False,
        notes=""
    )
    assert calculate_score(boat) < 80
