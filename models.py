from typing import List , Optional
from uuid import UUID, uuid4
from pydantic import BaseModel , Field
from enum import Enum

class Gender( str, Enum):
    male = "Male"
    female = "Female"
class user_profile(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name : str
    last_name : str
    elo : int
    gender: Gender

class Update_user_info(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
   
    
    
    
    
    
    