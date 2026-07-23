from __future__ import annotations

from typing import Any

from core.models import Boat
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
    def __init__(self, providers: list[Provider] | None = None):
        self.providers = providers or [
            CraigslistProvider(),
            BoatsComProvider(),
            UsedCaProvider(),
            CastanetProvider(),
            AutoTraderProvider(),
        ]
        self.last_provider_results: list[tuple[str, int]] = []

    def hunt(self, criteria: dict[str, Any] | None = None, status_callback=None) -> list[Boat]:
        results: list[Boat] = []
        provider_results: list[tuple[str, int]] = []

        for provider in self.providers:
            try:
                boats = provider.search(criteria)
            except Exception:
                boats = []

            provider_results.append((provider.name, len(boats)))
            if status_callback is not None:
                status_callback(provider.name, len(boats))
            for boat in boats:
                if boat.score == 0:
                    boat.score = calculate_score(boat)
                results.append(boat)

        unique_results: list[Boat] = []
        seen: set[tuple[str, str]] = set()
        for boat in results:
            key = (boat.name.lower().strip(), boat.location.lower().strip())
            if key in seen:
                continue
            seen.add(key)
            unique_results.append(boat)

        unique_results.sort(key=lambda boat: boat.score, reverse=True)
        self.last_provider_results = provider_results
        return unique_results
