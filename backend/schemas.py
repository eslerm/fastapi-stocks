from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from backend.database import Base


class SymbolSchema(Base):
    __tablename__ = "symbols"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String)
    exchange = Column(String)
    prices = relationship("HistorySchema")


class HistorySchema(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    symbol_id = Column(Integer, ForeignKey("symbols.id"))
    date = Column(Date)
    open = Column(Numeric(10, 2))
    high = Column(Numeric(10, 2))
    low = Column(Numeric(10, 2))
    close = Column(Numeric(10, 2))
    volume = Column(Integer)
