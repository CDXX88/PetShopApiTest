from enum import Enum
from typing import List
from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class PetStatus(str, Enum):
    available = "available"
    pending   = "pending"
    sold      = "sold"

class ApiResponse(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: PetStatus