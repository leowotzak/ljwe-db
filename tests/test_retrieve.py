import pytest
import requests
import re

from ljwedb.retrieve import COL_NAMES, SLICES, daily_equity_data


def test_column_names():
    assert type(COL_NAMES) is dict
    assert all(
        [isinstance(k, str) and isinstance(v, str) for k, v in COL_NAMES.items()]
    )


def test_slices():
    assert type(SLICES) is list
    assert all([bool(re.match(r"year\d+month\d+", slice_)) for slice_ in SLICES])


def test_daily_equity_data():

    # Cases
    # 1) symbol isn't string
    # 2) symbol is string but isn't a ticker
    # 3) symbol is a string and a ticker but doesn't exist
    # 4) symbol is string and does exist

    assert daily_equity_data(1) is AssertionError
    y = daily_equity_data("@thisis!no")
    z = daily_equity_data("AAZEESAKKEP")
    zz = daily_equity_data("AVB")
    zzz = daily_equity_data("AVBddd")
    zzzz = daily_equity_data("zxyAVB")

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "apikey": "JY78QD96PHNCLF5D",
    }

    t = requests.get("https://www.alphavantage.co/query", params=params)
    print(t.content)

    pass
