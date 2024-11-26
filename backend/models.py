from typing import Optional
from uuid import UUID, uuid4
from datetime import date
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str = Field(..., unique=True)
    rating: int
    release_date: date
    description: Optional[str] = None

class MovieUpdateRequest(BaseModel):
    name: Optional[str]
    rating: Optional[int]
    release_date: Optional[date]
    description: Optional[str] = None

