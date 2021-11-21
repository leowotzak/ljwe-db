import pytest
import requests
import re

import pandas as pd

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
    with pytest.raises(AssertionError) as e_info:
        daily_equity_data(1)
        daily_equity_data("@thisis!no")
        daily_equity_data("AVBddd")
        daily_equity_data("zxyAVB")
        daily_equity_data("AAZEESAKKEP")

    valid = daily_equity_data("AVB")
    assert isinstance(valid, pd.DataFrame)
    assert all(col in COL_NAMES.values() for col in valid.columns)
