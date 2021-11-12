
import pandas as pd
import requests
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


def _get_listed_symbols() -> pd.DataFrame:
    """Retrieves currently listed symbols from alphavantage"""
    res = requests.get(Config.base_url, params=_generate_query("LISTING_STATUS"))
    csv = str(res.content, encoding="utf-8")
    return pd.read_csv(csv, header=0)

