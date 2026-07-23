# Boat Hunter AI

Boat Hunter AI is a Streamlit-based workspace for tracking cabin cruiser opportunities, managing a local inventory, and preparing a provider-driven hunt framework.

## Current architecture
- app.py hosts the Streamlit entry point and multipage navigation.
- core/ contains the database, models, and scoring logic.
- providers/ contains provider interfaces and provider placeholders.
- services/ contains orchestration logic such as the SearchManager.
- pages/ contains dashboard, inventory, hunt, analytics, and settings views.
- tests/ contains regression tests for the core model and hunt flow.

## Development notes
- The inventory and CRUD flow remain the primary data-management path.
- The hunt flow is modular and ready for future provider implementation.
- Keep provider modules free of Streamlit and SQLite dependencies.
