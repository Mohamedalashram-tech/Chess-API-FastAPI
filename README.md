# ♟️ Chess Matchmaking API

This is a **FastAPI** project that manages chess players and handles matchmaking based on Elo ratings.

## 🌟 Key Features
- **Auto-ID:** Generates unique `UUID4` for every player automatically.
- **Data Persistence:** Saves all players in a `chess_db.json` file so data isn't lost.
- **Smart Matchmaking:** Logic to pair players based on their skill level.
- **Full CRUD:** Create, Read, Update, and Delete players via a clean API.

## 🚀 How to set up
1. Clone the repository.
2. Install FastAPI and Uvicorn: `pip install fastapi uvicorn`.
3. Start the server: `uvicorn chess:app --reload`.
4. Visit `/docs` to see the interactive Swagger UI.
