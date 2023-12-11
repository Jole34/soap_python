from pydantic import BaseModel
from typing import Optional

class UserToReturn(BaseModel):
    id: int
    email: Optional[str] = None
    age: int
    name: str

    class Config:
        orm_mode = True