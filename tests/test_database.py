import os

from core import database as dbmodule
from core.models import Boat


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
