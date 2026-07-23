from __future__ import annotations

from typing import Any, Callable

from core.models import Boat, SearchCriteria
from core.scoring import calculate_score
from providers import (
    AutoTraderProvider,
    BoatsComProvider,
    CastanetProvider,
    CraigslistProvider,
    Provider,
    UsedCaProvider,
)


class SearchManager:
    """Coordinate provider execution and merge scored boat results."""

    def __init__(self, providers: list[Provider] | None = None):
        self.providers = providers or [
            CraigslistProvider(),
            BoatsComProvider(),
            UsedCaProvider(),
            CastanetProvider(),
            AutoTraderProvider(),
        ]
        self.last_provider_results: list[tuple[str, int]] = []

    def hunt(
        self,
        profile: SearchCriteria | None = None,
        status_callback: Callable[[str, int], None] | None = None,
    ) -> list[Boat]:
        """Run each provider, merge results, remove duplicates, and score boats."""
        combined_results: list[Boat] = []
        provider_results: list[tuple[str, int]] = []

        for provider in self.providers:
            try:
                boats = provider.search(profile)
            except Exception:
                boats = []

            provider_results.append((provider.name, len(boats)))
            if status_callback is not None:
                status_callback(provider.name, len(boats))

            for boat in boats:
                if boat.score == 0:
                    boat.score = calculate_score(boat)
                combined_results.append(boat)

        unique_results = self._deduplicate_results(combined_results)
        unique_results.sort(key=lambda boat: boat.score, reverse=True)
        self.last_provider_results = provider_results
        return unique_results

    @staticmethod
    def _deduplicate_results(boats: list[Boat]) -> list[Boat]:
        unique_results: list[Boat] = []
        seen: set[tuple[str, str]] = set()

        for boat in boats:
            key = (boat.name.lower().strip(), boat.location.lower().strip())
            if key in seen:
                continue
            seen.add(key)
            unique_results.append(boat)

        return unique_results
