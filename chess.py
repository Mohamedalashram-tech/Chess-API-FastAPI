from fastapi import FastAPI , HTTPException
from models import user_profile , Update_user_info , Gender
from uuid import UUID, uuid4
from typing import List, Optional
from Users import db , save_to_json



app = FastAPI()


        
@app.get("/")
async def root():
    return {"Welcome to the main menu of the chess api"}

@app.get("/api/v1/chess")
async def fetch_all_users():
    return db

@app.post("/api/v1/chess")
async def create_user(user : user_profile):
    db.append(user)
    save_to_json()
    return {"Added Player :" : user.first_name + " " + user.last_name}

@app.delete("/api/v1/chess/{user_id}")
async def delete_user(user_id: UUID): 
    for user in db:
        if user.id == user_id: 
            db.remove(user)
            save_to_json()
            return {"message": "Player deleted"}
   
    raise HTTPException(status_code=404 , detail="Player not found")  

@app.put("/api/v1/chess/{user_id}")
async def update_user(user_id: UUID, user_update: Update_user_info):
    for user in db:
        if user.id == user_id:
           if user_update.first_name is not None:
                user.first_name = user_update.first_name
           if user_update.last_name is not None:
                user.last_name = user_update.last_name
        return {"message": "User updated successfully"}
    
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} not found"
    )

@app.get("/api/v1/chess/Leaderboard")
async def Show_Leaderboard():
    sorted_db = sorted(db, key=lambda x: x.elo,  reverse=True)
    return sorted_db

@app.get("/api/v1/chess/filter_by_gender")
async def fillter(gender: Gender):
    return [user for user in db if user.gender == gender]

@app.get("/api/v1/chess/matchmaking/{user_id}")
async def find_match(user_id: UUID):
    current_player = next((user for user in db if user.id == user_id), None)
    
    if not current_player:
        raise HTTPException(status_code=404, detail="Player not found")

    opponents = [user for user in db if user.id != user_id]
    
    
    if not opponents:
        raise HTTPException(status_code=404, detail="No other players available")

     
    best_match = min(opponents, key=lambda x: abs(x.elo - current_player.elo))

    return {
        "match_found": True,
        "opponent": best_match,
        "elo_diff": abs(best_match.elo - current_player.elo)
    }
    