from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.staticfiles import StaticFiles

from typing import Optional, Any
from pathlib import Path

from backend.schemas import Crude, History
from backend.data import CRUDE


backend = FastAPI(title="Oil Price Day")

api_router = APIRouter()


@api_router.get("/", status_code=200, response_model=list[Crude])
def root(request: Request) -> dict:
    return CRUDE

@api_router.get("/crude/{crude_label}", status_code=200, response_model=Crude)
def fetch_crude(*, crude_label: str) -> Any:
    result = [crude for crude in CRUDE if crude["label"] == crude_label]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Crude with ID {crude_label} not found"
        )
    return result[0]

@api_router.get("/crude/{crude_label}/history", status_code=200, response_model=list[History])
def fetch_crude(*, crude_label: str) -> Any:
    raw = [crude for crude in CRUDE if crude["label"] == crude_label]
    if not raw:
        raise HTTPException(
            status_code=404, detail=f"Crude with ID {crude_label} not found"
        )
    result = {'date': list(), 'price': list()}
    result = []
    for d in raw[0]['history']:
        result.append({'date': d['date'], 'price': d['price']})
    return result


backend.include_router(api_router)
