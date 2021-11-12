from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Equities(Base):

    __tablename__ = 'equities'
    equity_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    ticker = Column(String)
    description = Column(String)
    sector = Column(String)
    asset_type = Column(String)
    created_date = Column(DateTime)
    last_updated_date = Column(DateTime)