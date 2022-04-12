from pydantic import BaseModel
from datetime import date

# from typing import Sequence, List


class Symbol(BaseModel):
    #id: int
    #symbol: str
    value: str
    #name: str
    label: str
    #exchange: str

class Info(BaseModel):
    symbol: str
    name: str

class SymbolRequest(BaseModel):
    symbol: str


class History(BaseModel):
    date: date
    price: float
