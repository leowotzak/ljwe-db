import pytest
import requests
import re

import pandas as pd

from ljwedb.retrieve import COL_NAMES, SLICES, daily_equity_data
from ljwedb.retrieve import (
    daily_equity_data,
    weekly_equity_data,
    monthly_equity_data,
    intraday_equity_data_interval,
    intraday_equity_data_interval_extended,
)

from ljwedb.update import INTRADAY_MODELS


def test_column_names():
    assert type(COL_NAMES) is dict
    assert all(
        [isinstance(k, str) and isinstance(v, str) for k, v in COL_NAMES.items()]
    )


def test_slices():
    assert type(SLICES) is list
    assert all([bool(re.match(r"year\d+month\d+", slice_)) for slice_ in SLICES])


@pytest.mark.parametrize(
    "func", [daily_equity_data, weekly_equity_data, monthly_equity_data]
)
def test_equity_data(func):
    with pytest.raises(AssertionError) as e_info:
        func(1)
        func("@thisis!no")
        func("AVBddd")
        func("zxyAVB")
        func("AAZEESAKKEP")

    valid = func("AVB")
    assert isinstance(valid, pd.DataFrame)
    assert all(col in COL_NAMES.values() for col in valid.columns)


@pytest.mark.parametrize("interval", INTRADAY_MODELS.keys())
def test_intraday_equity_data(interval):

    with pytest.raises(AssertionError) as e_info:
        intraday_equity_data_interval(1, interval)
        intraday_equity_data_interval("@thisis!no", interval)
        intraday_equity_data_interval("AVBddd", interval)
        intraday_equity_data_interval("zxyAVB", interval)
        intraday_equity_data_interval("AAZEESAKKEP", interval)

    valid = intraday_equity_data_interval("AVB", interval)
    assert isinstance(valid, pd.DataFrame)
    assert all(col in COL_NAMES.values() for col in valid.columns)


@pytest.mark.parametrize("interval", INTRADAY_MODELS.keys())
def test_intraday_equity_extended_data(interval):
    pass
