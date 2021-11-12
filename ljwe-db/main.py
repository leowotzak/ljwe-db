
import pandas as pd
import requests
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

