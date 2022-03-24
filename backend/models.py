from pydantic import BaseModel

# from typing import Sequence, List


class Future(BaseModel):
    id: int
    symbol: str
    name: str
    exchange: str


class FutureRequest(BaseModel):
    symbol: str


class History(BaseModel):
    id: int
