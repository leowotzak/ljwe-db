from config import Config
from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(Config.database_url)
SESSION = sessionmaker(engine)


Base = declarative_base()


class Symbols(Base):
    """Model used for different securities i.e. stocks, bonds, ETFs etc..."""

    __tablename__ = "symbols"

    symbol_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    ticker = Column(String, nullable=False)
    description = Column(String)
    sector = Column(String)
    asset_type = Column(String)
    created_date = Column(DateTime, nullable=False)
    last_updated_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Equity id={self.symbol_id} name={self.name} ticker={self.ticker}>"


class BarDataDaily(Base):

    __tablename__ = "bar_data_daily"

    timestamp = Column(DateTime, primary_key=True)
    symbol_id = Column(Integer, primary_key=True)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    adj_close_price = Column(Float)
    volume = Column(Integer, nullable=False)
    dividend_amount = Column(Float)

    def __repr__(self):
        return f"<BarDataDaily id={self.equity_id} ts={self.timestamp}>"
