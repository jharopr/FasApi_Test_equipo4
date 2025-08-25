from pydantic import BaseModel
from typing import Optional

#dto

class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    phone: str  