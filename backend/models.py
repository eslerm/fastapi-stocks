from pydantic import BaseModel
from datetime import date

# from typing import Sequence, List


class Symbol(BaseModel):
    id: int
    symbol: str
    name: str
    exchange: str


class SymbolRequest(BaseModel):
    symbol: str


class History(BaseModel):
    date: date
    price: float
