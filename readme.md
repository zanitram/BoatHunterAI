# Boat Hunter AI

## Overview
Boat Hunter AI is a Streamlit-based workspace for tracking cabin cruiser opportunities, managing a local inventory, and running a provider-driven hunt workflow.

The application currently focuses on a polished local experience with SQLite-backed boat inventory management, dashboard metrics, and a modular search framework that can evolve into live provider integrations.

## Installation
1. Create and activate a virtual environment if desired.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Python 3.10+ is available.

## Running the app
Run the application with:

```bash
streamlit run app.py
```

## Folder structure
- app.py — Streamlit entry point and multipage navigation
- core/ — database, models, and scoring logic
- pages/ — dashboard, inventory, search profile, hunt, analytics, and settings views
- providers/ — provider interfaces and placeholders
- services/ — hunt orchestration and search management
- tests/ — regression tests
- data/ — SQLite database output

## Screenshots
Screenshots will be added as the interface evolves. The current UI includes:
- Dashboard overview
- Inventory management
- Search profile management
- Hunt workflow

## Roadmap
See [ROADMAP.md](ROADMAP.md) for current milestones and planned work.

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for release history.

## Development notes
- The inventory and CRUD flow remain the primary data-management path.
- The hunt flow is modular and ready for future provider implementation.
- Keep provider modules free of Streamlit and SQLite dependencies.
