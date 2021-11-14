"""models.py

Database models utilized by DB scripts to query/add new entries



"""
from sqlalchemy import Column, DateTime, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///app.db")
SESSION = sessionmaker(engine)


Base = declarative_base()


class Equities(Base):
    """Equity model used for stocks and ETFs"""

    __tablename__ = "equities"

    equity_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    ticker = Column(String, nullable=False)
    description = Column(String)
    sector = Column(String)
    asset_type = Column(String)
    created_date = Column(DateTime, nullable=False)
    last_updated_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Equity id={self.equity_id} name={self.name} ticker={self.ticker}>"


class BarData(Base):
    """Data model for 'Bar' i.e. an equity price snapshot"""

    __tablename__ = "daily_bar_data"

    equity_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    adj_close_price = Column(Float)
    volume = Column(Integer, nullable=False)
    dividend_amount = Column(Float)

    def __repr__(self):
        return f"<BarData id={self.equity_id} ts={self.timestamp}>"
