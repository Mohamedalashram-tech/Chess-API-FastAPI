
from typing import List, Optional
from models import user_profile , Update_user_info , Gender
from uuid import UUID, uuid4
import json
import os

DB_FILE = "chess_db.json"

db : List[user_profile] = [
    user_profile(
        id = UUID( "c588183e-2dca-410c-949c-ea194024aaf1"),
        first_name="Mohamed",
        last_name="Alashram",
        gender = Gender.male ,
        elo = 1200
    ),
    user_profile(
        id = UUID( "3b0ca49f-3113-4a52-8172-b22238dac692"),
        first_name="Aymen",
        last_name="Ebrahim",
        gender = Gender.male ,
        elo = 2200
    ),
    user_profile(
        id = UUID( "3b0ca49f-3113-4a52-8172-b22238dac699"),
        first_name="Salma",
        last_name="Eid",
        gender = Gender.female ,
        elo = 1350
    ),
    user_profile(
        id = UUID( "3b0ca49f-3113-4a52-8172-b22238dac691"),
        first_name="Reem",
        last_name="Malek",
        gender = Gender.female ,
        elo = 2565
    )
    
]

def save_to_json():
    serializable_db = [user.dict() for user in db]
    for user in serializable_db:
        user['id'] = str(user['id'])
        user['gender'] = user['gender'].value 
    
    with open(DB_FILE, "w", encoding='utf-8') as f:
        json.dump(serializable_db, f, indent=4)

def load_from_json():
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, "r", encoding='utf-8') as f:
        data = json.load(f)
        return [user_profile(**user) for user in data]

db = load_from_json()