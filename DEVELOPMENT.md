# Development Notes

## Milestone 4: Search Profiles

The search flow now uses reusable SearchCriteria objects instead of hardcoded criteria dictionaries.

### Key pieces
- core/models.py defines SearchCriteria for budget, distance, length, brand, engine, freshwater, and trailer preferences.
- core/database.py stores profiles in SQLite in the search_profiles table with create, read, update, and delete support.
- pages/search_profiles.py provides the full CRUD UI.
- pages/hunt.py lets users choose a saved profile before running the hunt.
- services/search_manager.py accepts a SearchCriteria object in hunt(profile).

### Testing
- Run the regression suite with: pytest -q tests/test_database.py tests/test_scoring.py tests/test_search_manager.py
