from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
from sqlalchemy.orm import Session
import yfinance as yf
from typing import List
# from typing import Any, Optional
from backend.database import Base, engine, get_db, SessionLocal
from backend.schemas import SymbolSchema, HistorySchema
from backend.models import History, Info, Symbol, SymbolRequest


def yf_create_symbol(id: int):
    db = SessionLocal()
    symbol = db.query(SymbolSchema).filter(SymbolSchema.id == id).first()
    yd = yf.Ticker(symbol.symbol)
    symbol.name = yd.info["shortName"]
    symbol.exchange = yd.info["exchange"]
    db.add(symbol)
    db.commit()
    df = yd.history(period="max")
    #df = yd.history(period="1wk")
    for index, row in df.iterrows():
        h = HistorySchema()
        h.symbol_id = symbol.id
        h.date = index.date()
        h.open = round(float(row["Open"]), 2)
        h.high = round(float(row["High"]), 2)
        h.low = round(float(row["Low"]), 2)
        h.close = round(float(row["Close"]), 2)
        h.volume = int(row["Volume"])
        db.add(h)
        db.commit()
    print(f"{symbol.symbol} added")


app = FastAPI()
router = APIRouter()
Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@router.get("/symbols", status_code=200, response_model=list[Symbol])
async def fetch_symbols():
    db = SessionLocal()
    all_symbols = db.query(SymbolSchema)
    res = [
        {"value": f.symbol, "label": f.name}
        for f in all_symbols
    ]
    return res


@router.post("/create_symbol")
async def create_symbol(
    symbol_request: SymbolRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    add symbol to database

    TODO: add error handling
          e.g., stock doesn't exist/cannot be updated
          currently a bad symbol will break api
          what do repeat symbols do?
          force ALPHA
    """
    symbol = SymbolSchema()
    symbol.symbol = symbol_request.symbol
    db.add(symbol)
    db.commit()
    background_tasks.add_task(yf_create_symbol, symbol.id)
    return {"code": f"added {symbol.symbol}"}


@router.get("/info/{symbol}", status_code=200, response_model=Info)
async def fetch_symbol(symbol: str):
    """
    get symbol info
    """
    db = SessionLocal()
    s = db.query(SymbolSchema).filter(SymbolSchema.symbol == symbol).first()
    res = {"symbol": s.symbol, "name": s.name}
    return res


@router.get("/history/{symbol}", status_code=200, response_model=list[History])
async def fetch_symbol(symbol: str):
    """
    get symbol price history
    """
    db = SessionLocal()
    s = db.query(SymbolSchema).filter(SymbolSchema.symbol == symbol).first()
    all_history = db.query(HistorySchema).filter(HistorySchema.symbol_id == s.id).all()
    res = [{"date": h.date, "price": h.close} for h in all_history]
    return res


app.include_router(router)
