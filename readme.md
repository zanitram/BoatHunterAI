# Boat Hunter AI

Boat Hunter AI is a Streamlit-based workspace for tracking cabin cruiser opportunities, managing a local inventory, and running a provider-driven hunt workflow.

## Current architecture
- app.py hosts the Streamlit entry point and multipage navigation.
- core/ contains the database, models, and scoring logic.
- providers/ contains provider interfaces and provider placeholders.
- services/ contains orchestration logic such as the SearchManager.
- pages/ contains dashboard, inventory, search-profile, hunt, analytics, and settings views.
- tests/ contains regression tests for the core model and hunt flow.

## Milestone 4 highlights
- Search Profiles provide reusable budget, distance, length, brand, engine, freshwater, and trailer preferences.
- Profiles are stored in SQLite so they can be created, edited, deleted, and reused across hunts.
- The Hunt page lets users select a saved profile before launching a search.

## Development notes
- The inventory and CRUD flow remain the primary data-management path.
- The hunt flow is modular and ready for future provider implementation.
- Keep provider modules free of Streamlit and SQLite dependencies.
