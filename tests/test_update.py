import pytest

from ljwedb.update import PER_REQUEST_WAIT, INTRADAY_MODELS
from ljwedb.models import (
    bar_data_1min,
    bar_data_5min,
    bar_data_15min,
    bar_data_30min,
    bar_data_1h,
)

DB_MODELS = [bar_data_1min, bar_data_5min, bar_data_15min, bar_data_30min, bar_data_1h]


def test_request_wait():
    assert isinstance(PER_REQUEST_WAIT, int)
    assert 0 < PER_REQUEST_WAIT <= 60


@pytest.mark.parametrize("model", INTRADAY_MODELS.items())
def test_intraday_models(model):
    assert isinstance(interval, str)
    assert model in DB_MODELS
