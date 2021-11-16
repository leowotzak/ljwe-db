"""LJWE DB.

A collection of functions that facilitate the creating, updating, and appending the 
master securities database. The scripts use pandas to format the data properly and 
requests to parse http requests/responses.

Input

    None

Output

    None



"""

import json
import logging
import time
from datetime import datetime
from io import StringIO

import pandas as pd
import requests
from config import Config
from models import SESSION, BarDataDaily, Equities

logging.basicConfig(filename="main.log", filemode="a", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

COL_NAMES = {
    "1. open": "open_price",
    "2. high": "high_price",
    "3. low": "low_price",
    "4. close": "close_price",
    "5. volume": "volume",
}

INTERVALS = ["1min", "5min", "15min", "30min", "60min"]

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


def bar_data_wrapper(func):
    """Standardizes column names for any bar data"""

    def wrapper(*args, **kwargs):
        res: pd.DataFrame = func(*args, **kwargs)
        return res.rename(columns=COL_NAMES)

    return wrapper


def _generate_query(
    function: str,
    symbol: str = None,
    interval: str = None,
    slice_: str = None,
    outputsize: bool = False,
    datatype: bool = False,
) -> dict:
    """Produces an appropriate parameter set for each endpoint"""

    function = function + "_ADJUSTED" if Config.adjusted else function

    params = {
        "function": function,
        "apikey": Config.api_key,
    }

    if symbol:
        params["symbol"] = symbol

    if interval:
        params["interval"] = interval

    if slice_:
        params["slice"] = slice_

    if outputsize:
        params["output_size"] = Config.output_size

    if datatype:
        params["data_type"] = Config.data_type

    log.debug(params)

    return params


def _get_database_symbols() -> list:
    """Queries database for current symbols"""
    with SESSION() as session:
        return session.query(Equities).all()


def _get_listed_symbols() -> pd.DataFrame:
    """Retrieves currently listed symbols from alphavantage"""
    res = requests.get(Config.base_url, params=_generate_query("LISTING_STATUS"))
    csv = str(res.content, encoding="utf-8")
    return pd.read_csv(StringIO(csv), header=0)


@bar_data_wrapper
def _get_daily_equity_data(symbol: str) -> pd.DataFrame:
    """Requests daily bar data for the provided symbol from alphavantage"""

    params = _generate_query(
        "TIME_SERIES_DAILY", symbol=symbol, outputsize=True, datatype=True
    )

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()["Time Series (Daily)"]), orient="index")


@bar_data_wrapper
def _get_weekly_equity_data(symbol: str) -> pd.DataFrame:
    """Requests weekly bar data for the provided symbol"""

    params = _generate_query("TIME_SERIES_WEEKLY", symbol=symbol, datatype=True)

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()["Weekly Time Series"]), orient="index")


@bar_data_wrapper
def _get_monthly_equity_data(symbol: str) -> pd.DataFrame:
    """Requests monthly bar data for the provided symbol"""

    params = _generate_query("TIME_SERIES_MONTHLY", symbol=symbol, datatype=True)

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()["Monthly Time Series"]), orient="index")


@bar_data_wrapper
def _get_intraday_equity_data_interval(symbol: str, interval: str) -> pd.DataFrame:
    """Requests intraday (or extended intraday) bar info for provided symbol at given interval"""

    params = _generate_query(
        "TIME_SERIES_INTRADAY",
        symbol=symbol,
        interval=interval,
        outputsize=True,
        datatype=True,
    )

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()[f"Time Series ({interval})"])).transpose()


@bar_data_wrapper
def _get_intraday_equity_data_interval_extended(
    symbol: str, interval: str, slice_: str
) -> pd.DataFrame:
    """Requests intraday (extended) bar info for provided symbol at given interval for each slice"""

    params = _generate_query(
        "TIME_SERIES_INTRADAY_EXTENDED", symbol=symbol, interval=interval, slice=slice_
    )
    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()[""]))


def _get_intraday_equity_data(symbol: str):
    """Wrapper function that gets intraday data at all intervals"""
    for interval in INTERVALS:
        log.debug("Using interval: %s", interval)
        print(_get_intraday_equity_data_interval(symbol, interval).head(10))


def _get_intraday_equity_data_extended(symbol: str):
    """Wrapper function that gets intraday data history at all slices"""
    return


def _insert_bars_to_table(*dfs):
    """Takes a bar data DataFrame and inserts the bars into the proper table"""
    for df in dfs:
        for equity_id, bar_data in df.iterrows():
            print(1)


def update_equities():
    """Adds/updates symbols table with data from alphavantage"""
    with SESSION() as session:
        for equity_id, bar_data in _get_listed_symbols().iterrows():
            ts = datetime.utcnow()
            bar = Equities(
                equity_id=equity_id,
                name=bar_data["name"],
                ticker=bar_data["symbol"],
                asset_type=bar_data["assetType"],
                created_date=ts,
                last_updated_date=ts,
            )
            log.debug("Adding symbol %s to database", bar)
            session.merge(bar)
        log.debug("Committing session...")
        session.commit()


def update_prices():
    """Adds/updates price data for each symbol in symbols table"""
    with SESSION() as session:
        for equity_id, bar_data in _get_listed_symbols().iterrows():
            for get_func in (
                _get_daily_equity_data,
                _get_weekly_equity_data,
                _get_monthly_equity_data,
            ):
                price_data = get_func(bar_data["symbol"])
                for ts, b in price_data.iterrows():
                    bar = BarDataDaily(equity_id=equity_id, timestamp=ts, **b)
                    log.debug(bar)
                    session.merge(bar)
                log.debug("Committing for %s", bar_data["symbol"])
                session.commit()
                time.sleep(15)


if __name__ == "__main__":
    update_prices()
