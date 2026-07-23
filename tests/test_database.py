import os

from core import database as dbmodule
from core.models import Boat, SearchCriteria


def test_initialize_and_crud(tmp_path):
    db_path = tmp_path / "boats.db"
    dbmodule.DATABASE = str(db_path)

    dbmodule.initialize()

    assert os.path.exists(db_path)

    boat = Boat(
        name="Sea Ray 240",
        price=12500,
        location="Toronto",
        engine="5.0 MPI",
        length=24.5,
        trailer=True,
        notes="Great starter cruiser"
    )

    dbmodule.add_boat(boat)
    boats = dbmodule.get_boats()
    assert len(boats) == 1

    boat_id = boats[0][0]
    dbmodule.update_boat(
        boat_id,
        price=13000,
        location="Hamilton",
        notes="Updated after inspection"
    )

    updated = dbmodule.get_boats()[0]
    assert updated[2] == 13000
    assert updated[3] == "Hamilton"
    assert updated[8] == "Updated after inspection"

    dbmodule.delete_boat(boat_id)
    assert dbmodule.get_boats() == []


def test_search_profile_crud(tmp_path):
    db_path = tmp_path / "boats.db"
    dbmodule.DATABASE = str(db_path)
    dbmodule.initialize()

    profile = SearchCriteria(
        name="Weekend cruiser",
        budget_min=8000,
        budget_max=15000,
        max_distance_km=250,
        length_min=20,
        length_max=30,
        brands="Sea Ray, Bayliner",
        engine_preferences="Outboard, Inboard",
        freshwater_only=True,
        trailer_required=True,
    )

    profile_id = dbmodule.add_search_profile(profile)
    assert profile_id is not None

    stored = dbmodule.get_search_profile(profile_id)
    assert stored is not None
    assert stored.name == "Weekend cruiser"
    assert stored.budget_min == 8000
    assert stored.budget_max == 15000
    assert stored.max_distance_km == 250

    dbmodule.update_search_profile(
        profile_id,
        budget_max=18000,
        freshwater_only=False,
    )

    updated = dbmodule.get_search_profile(profile_id)
    assert updated.budget_max == 18000
    assert updated.freshwater_only is False

    dbmodule.delete_search_profile(profile_id)
    assert dbmodule.get_search_profile(profile_id) is None