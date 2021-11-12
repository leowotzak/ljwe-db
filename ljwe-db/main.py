
import pandas as pd
import requests

import json

from models import Equities, SESSION
from config import Config
COL_NAMES = {
    '1. open': 'open_price',
    '2. high': 'high_price', 
    '3. low': 'low_price',
    '4. close': 'close_price',
    '5. volume': 'volume',
}




def bar_data_wrapper(func):
    """Standardizes column names for any bar data"""
    def wrapper(*args, **kwargs):
        res: pd.DataFrame = func(*args, **kwargs)
        return res.rename(columns=COL_NAMES)   
    return wrapper


def _generate_query(
    function: str, symbol: str = None, outputsize: bool = False, datatype: bool = False
) -> dict:
    """Produces an appropriate parameter set for each endpoint"""

    params = {
        "function": function,
        "apikey": Config.api_key,
    }

    if symbol:
        params["symbol"] = symbol

    if outputsize:
        params["output_size"] = Config.output_size

    if datatype:
        params["data_type"] = Config.data_type

    return params


def _get_database_symbols(): # type hint for return type
    """Queries database for current symbols"""
    with SESSION() as session:
        return session.query(Equities).all()


def _get_listed_symbols() -> pd.DataFrame:
    """Retrieves currently listed symbols from alphavantage"""
    res = requests.get(Config.base_url, params=_generate_query("LISTING_STATUS"))
    csv = str(res.content, encoding="utf-8")
    return pd.read_csv(csv, header=0)


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
    """Requests weekly bar data for the provided symbol from alphavantage"""

    params = _generate_query(
        "TIME_SERIES_WEEKLY", symbol=symbol, datatype=True
    )

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()["Weekly Time Series"]), orient="index")


@bar_data_wrapper
def _get_monthly_equity_data(symbol: str) -> pd.DataFrame:
    """Requests weekly bar data for the provided symbol from alphavantage"""

    params = _generate_query(
        "TIME_SERIES_MONTHLY", symbol=symbol, datatype=True
    )

    res = requests.get(Config.base_url, params=params)
    return pd.read_json(json.dumps(res.json()["Monthly Time Series"]), orient="index")


def update_equities():
    """Adds/updates database with data from alphavantage"""

    for id, bar in _get_listed_symbols().iterrows():
        print(id, bar)
        # Add / update
