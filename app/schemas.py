from pydantic import BaseModel, HttpUrl

from typing import Sequence, List

class History(BaseModel):
    date: str
    price: float

class Crude(BaseModel):
    id: int
    label: str
    country: str
