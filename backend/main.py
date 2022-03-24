from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    FastAPI,
)
import sqlalchemy
from sqlalchemy.orm import Session
import yfinance as yf
from typing import List

# from typing import Any, Optional

from backend.database import Base, engine, get_db, SessionLocal
from backend.schemas import FutureSchema, HistorySchema
from backend.models import Future, FutureRequest, History


def yf_create_future(id: int):
    db = SessionLocal()
    future = db.query(FutureSchema).filter(FutureSchema.id == id).first()
    yd = yf.Ticker(future.symbol)
    future.name = yd.info["shortName"]
    future.exchange = yd.info["exchange"]
    df = yd.history(period="max")
    for index, row in df.iterrows():
        h = HistorySchema()
        h.future_id = future.id
        h.date = index.date()
        h.open = round(float(row["Open"]), 2)
        h.high = round(float(row["High"]), 2)
        h.low = round(float(row["Low"]), 2)
        h.close = round(float(row["Close"]), 2)
        h.volume = int(row["Volume"])
        db.add(h)
        db.commit()
    db.add(future)
    db.commit()


app = FastAPI()
router = APIRouter()
Base.metadata.create_all(bind=engine)


@router.get("/futures", status_code=200, response_model=list[Future])
async def fetch_future():
    db = SessionLocal()
    all_futures = db.query(FutureSchema)
    res = [
        {"id": f.id, "symbol": f.symbol, "name": f.name, "exchange": f.exchange}
        for f in all_futures
    ]
    return res


@router.post("/create_future")
async def create_future(
    future_request: FutureRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    add future to database
    """
    future = FutureSchema()
    future.symbol = future_request.symbol

    db.add(future)
    db.commit()

    background_tasks.add_task(yf_create_future, future.id)
    return {"code": f"added {future.symbol}"}


app.include_router(router)
