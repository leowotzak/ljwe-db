import logging
from datetime import datetime

from sqlalchemy.dialects.mysql import insert

from . import retrieve
from .config import Config
from .models import (
    SESSION,
    bar_data_daily,
    bar_data_weekly,
    bar_data_monthly,
    bar_data_1min,
    bar_data_5min,
    bar_data_15min,
    bar_data_30min,
    bar_data_1h,
)

log = logging.getLogger(__name__)


PER_REQUEST_WAIT = 15

INTRADAY_MODELS = {
    "1min": bar_data_1min,
    "5min": bar_data_5min,
    "15min": bar_data_15min,
    "30min": bar_data_30min,
    "60min": bar_data_1h,
}

SLICES = [
    "year1month1",
    "year1month2",
    "year1month3",
    "year1month4",
    "year1month5",
    "year1month6",
    "year1month7",
    "year1month8",
    "year1month9",
    "year1month10",
    "year1month11",
    "year1month12",
    "year2month1",
    "year2month2",
    "year2month3",
    "year2month4",
    "year2month5",
    "year2month6",
    "year2month7",
    "year2month8",
    "year2month9",
    "year2month10",
    "year2month11",
    "year2month12",
]


def daily_prices(symbol: str, symbol_id: int):
    with SESSION() as session:
        for ts, b in retrieve.daily_equity_data(symbol).iterrows():
            m = bar_data_daily(symbol_id=symbol_id, timestamp=ts, **b)
            session.merge(m)
        else:
            log.debug("Committing new daily price data for %s", symbol)
            session.commit()


def weekly_prices(symbol: str, symbol_id: int):
    with SESSION() as session:
        for ts, b in retrieve.weekly_equity_data(symbol).iterrows():
            m = bar_data_weekly(symbol_id=symbol_id, timestamp=ts, **b)
            session.merge(m)
        else:
            log.debug("Committing new weekly price data for %s", symbol)
            session.commit()


def monthly_prices(symbol: str, symbol_id: int):
    with SESSION() as session:
        for ts, b in retrieve.monthly_equity_data(symbol).iterrows():
            m = bar_data_monthly(symbol_id=symbol_id, timestamp=ts, **b)
            session.merge(m)
        else:
            log.debug("Committing new monthly price data for %s", symbol)
            session.commit()


def intraday_prices(symbol: str, symbol_id: int):
    with SESSION() as session:
        for interval, model in INTRADAY_MODELS.items():
            for ts, b in retrieve.intraday_equity_data_interval(
                symbol, interval
            ).iterrows():
                m = model(symbol_id=symbol_id, timestamp=ts, **b)
                session.merge(m)
            else:
                log.debug(
                    "Committing new intraday (%s) price data for %s", interval, symbol
                )
                session.commit()


def intraday_extended_history_prices(symbol, symbol_id):
    with SESSION() as session:
        for slice_ in SLICES:
            for interval, model in INTRADAY_MODELS.items():
                for ts, b in retrieve.intraday_equity_data_interval_extended(
                    symbol, interval, slice_
                ).iterrows():
                    m = model(symbol_id=symbol_id, timestamp=ts, **b)
                    session.merge(m)
                else:
                    log.debug(
                        "Committing new intraday extended (%s) price data for %s",
                        interval,
                        symbol,
                    )
                    session.commit()
                time.sleep(PER_REQUEST_WAIT)
