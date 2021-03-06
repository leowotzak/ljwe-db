"""Namespace of functions that retrieve and format data from alpha vantage

Manufactures queries, and sends GET requests to alpha vantage. Extracted
results are transformed into a format that is recognized and loaded by 
the database schema.


"""
import json
import re
import logging
import importlib
from datetime import datetime
from io import StringIO
from typing import Generator

import pandas as pd
import requests


from .. import models
from .config import Config

log = logging.getLogger(__name__)

COL_NAMES = {
    "1. open": "open_price",
    "open": "open_price",
    "high": "high_price",
    "low": "low_price",
    "close": "close_price",
    "2. high": "high_price",
    "3. low": "low_price",
    "4. close": "close_price",
    "5. adjusted close": "adj_close_price",
    "5. volume": "volume",
    "6. volume": "volume",
    "7. dividend amount": "dividend_amount",
    "8. split coefficient": "split_coeff",
}


def Ticker(symbol: str) -> bool:
    """Type for valid ticker structures

    Constraints are: contiguous string of all caps letters
    """
    if isinstance(symbol, str):
        return True if bool(re.match(r"[A-Z]+", symbol)) else False
    else:
        return False


def bar_data_wrapper(func):
    """Standardizes column names for any bar data"""

    def wrapper(*args, **kwargs):
        assert Ticker(args[0])
        res: pd.DataFrame = func(*args, **kwargs)
        return res.rename(columns=COL_NAMES).iterrows()

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

    function = (
        function + "_ADJUSTED"
        if Config.adjusted and not "INTRADAY" in function
        else function
    )

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
        params["outputsize"] = Config.output_size

    if datatype:
        params["datatype"] = Config.data_type

    log.debug(params)

    return params


def database_symbols():
    """Queries database for current symbols"""
    # FIXME add types to generator
    for bar in models.Symbol.objects.all():
        yield bar


# def listed_symbols() -> pd.DataFrame:
#     """Retrieves currently listed symbols from alphavantage"""
#     res = requests.get(Config.base_url, params=_generate_query("LISTING_STATUS"))
#     csv = str(res.content, encoding="utf-8")
#     return pd.read_csv(StringIO(csv), header=0)


def wiki_sp500() -> pd.DataFrame:
    """Queries S&P 500 companies for simplicity & size constraints from DB"""
    members = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[
        0
    ]

    entries = [
        models.Symbol(
            name=bar["Security"],
            ticker=bar["Symbol"],
            sector=bar["GICS Sector"],
            asset_type=["stock"],
        )
        for idx, bar in members.iterrows()
    ]
    log.debug("Committing entries...")
    models.Symbol.objects.bulk_create(entries)


@bar_data_wrapper
def daily_equity_data(symbol: str) -> pd.DataFrame:
    """Requests daily bar data for the provided symbol from alphavantage"""

    params = _generate_query(
        "TIME_SERIES_DAILY", symbol=symbol, outputsize=True, datatype=True
    )

    res = requests.get(Config.base_url, params=params)
    assert "Error Message" not in res.json()

    return pd.read_json(json.dumps(res.json()["Time Series (Daily)"]), orient="index")


@bar_data_wrapper
def weekly_equity_data(symbol: str) -> pd.DataFrame:
    """Requests weekly bar data for the provided symbol"""

    params = _generate_query("TIME_SERIES_WEEKLY", symbol=symbol, datatype=True)

    res = requests.get(Config.base_url, params=params)

    if res.json().get("Weekly Time Series"):
        k = res.json().get("Weekly Time Series")
    elif res.json().get("Weekly Adjusted Time Series"):
        k = res.json().get("Weekly Adjusted Time Series")

    return pd.read_json(json.dumps(k), orient="index")


@bar_data_wrapper
def monthly_equity_data(symbol: str) -> pd.DataFrame:
    """Requests monthly bar data for the provided symbol"""

    params = _generate_query("TIME_SERIES_MONTHLY", symbol=symbol, datatype=True)

    res = requests.get(Config.base_url, params=params)
    log.debug(res.json())

    if res.json().get("Monthly Time Series"):
        k = res.json().get("Monthly Time Series")
    elif res.json().get("Monthly Adjusted Time Series"):
        k = res.json().get("Monthly Adjusted Time Series")

    return pd.read_json(json.dumps(k), orient="index")


@bar_data_wrapper
def intraday_equity_data_interval(symbol: str, interval: str) -> pd.DataFrame:
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
def intraday_equity_data_interval_extended(
    symbol: str, interval: str, slice_: str
) -> pd.DataFrame:
    """Requests intraday (extended) bar info for provided symbol at given interval for each slice"""

    params = _generate_query(
        "TIME_SERIES_INTRADAY_EXTENDED", symbol=symbol, interval=interval, slice_=slice_
    )

    res = requests.get(Config.base_url, params=params)
    df = pd.read_csv(StringIO(str(res.content, encoding="utf-8")), index_col=["time"])
    df.index = pd.to_datetime(df.index)
    return df
