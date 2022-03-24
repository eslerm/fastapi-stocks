from fastapi import (
    BackgroundTasks,
    Depends,
    FastAPI,
)
from pydantic import BaseModel
from sqlalchemy.orm import Session
import yfinance as yf
# from typing import Optional, Any

from backend.models import Future, History
from backend.database import Base, engine, get_db, SessionLocal
# from app.schemas import Crude, History


class FutureRequest(BaseModel):
    symbol: str


app = FastAPI()


Base.metadata.create_all(bind=engine)


def yf_add_data(id: int):
    db = SessionLocal()
    future = db.query(Future).filter(Future.id == id).first()
    yd = yf.Ticker(future.symbol)
    future.name = yd.info['shortName']
    future.exchange = yd.info['exchange']
    df = yd.history(period="max")
    for index, row in df.iterrows():
        h = History()
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


@app.post("/add")
async def create_future(
    future_request: FutureRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    add future to database
    """
    future = Future()
    future.symbol = future_request.symbol

    db.add(future)
    db.commit()

    background_tasks.add_task(yf_add_data, future.id)
    return {"code": f"added {future.symbol}"}
