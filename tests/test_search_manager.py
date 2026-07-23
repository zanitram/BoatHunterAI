from services.search_manager import SearchManager
from providers import CraigslistProvider
from core.models import Boat, SearchCriteria


def test_hunt_returns_deduped_boats_and_scores():
    class StubProvider(CraigslistProvider):
        name = "Stub"

        def search(self, criteria=None):
            return [
                Boat(name="Test Boat", price=9000, location="Toronto", engine="5.0 MPI", length=24, trailer=True, notes=""),
                Boat(name="Test Boat", price=9000, location="Toronto", engine="5.0 MPI", length=24, trailer=True, notes=""),
            ]

    manager = SearchManager(providers=[StubProvider()])
    results = manager.hunt(SearchCriteria(name="Test profile"))
    assert len(results) == 1
    assert results[0].score >= 0
