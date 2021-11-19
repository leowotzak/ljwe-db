"""Database Models

Currently contains the following:

    Symbol table to track each individual security & its metadata,
    see repo for a diagram

    Interday bar data:
        > daily
        > weekly
        > monthly

    Intraday bar data:
        > 1 minute
        > 5 minute
        > 15 minute
        > 30 minute
        > 60 minute


"""
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Text,
    create_engine,
    TIMESTAMP
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from .config import Config

engine = create_engine(Config.database_url)
SESSION = sessionmaker(engine)

meta = MetaData(naming_convention={
  "ix": 'ix_%(column_0_label)s',
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
})
Base = declarative_base(metadata=meta)


class Symbol(Base):
    """Model used for different securities i.e. stocks, bonds, ETFs etc..."""

    __tablename__ = 'symbol'

    symbol_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    ticker = Column(String(30), nullable=False)
    description = Column(Text)
    sector = Column(String(30))
    asset_type = Column(String(30))
    created_date = Column(DateTime, default=datetime.utcnow())
    last_updated_date = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    # ! I dont think this covers all the child tables
    children = relationship("bar_data_daily")

    def __repr__(self):
        return f"<Symbol id={self.symbol_id} name={self.name} ticker={self.ticker}>"


class BarData:
    """Contains security's information at a given time interval.

    For example, each day a stock has an open price, high price, low price, 
    and close price, in addition to the # of stocks sold during that day.

    This class is used as a mixin to organize time series data among different
    tables by frequency.
    """
    @declared_attr
    def symbol_id(cls):
        return Column(Integer, ForeignKey('symbol.symbol_id'), primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # I dont think its good to have two primary keys
    timestamp         = Column(DateTime, primary_key=True)
    
    open_price        = Column(Float, nullable=False)
    high_price        = Column(Float, nullable=False)
    low_price         = Column(Float, nullable=False)
    close_price       = Column(Float, nullable=False)
    adj_close_price   = Column(Float)
    volume            = Column(Integer, nullable=False)
    dividend_amount   = Column(Float)
    split_coeff       = Column(Float)
    created_date = Column(DateTime, default=datetime.utcnow())
    last_updated_date = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


# * Empty table classes since currently each table is identical
# * The name of each class determines the table name


class bar_data_daily(BarData, Base):
    pass


class bar_data_weekly(BarData, Base):
    pass


class bar_data_monthly(BarData, Base):
    pass


class bar_data_1min(BarData, Base):
    pass


class bar_data_5min(BarData, Base):
    pass


class bar_data_15min(BarData, Base):
    pass


class bar_data_30min(BarData, Base):
    pass


class bar_data_1h(BarData, Base):
    pass
