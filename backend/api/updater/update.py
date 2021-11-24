"""Namespace of functions that update the Database

Functions initialize a database session, request each alpha vantage
endpoint, and insert/update new data.

    note: each request has a hard-coded 15 second wait timer


"""
import logging
from datetime import datetime
import time
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .. import models

from . import retrieve
from .config import Config

log = logging.getLogger(__name__)

PER_REQUEST_WAIT = 15

INTRADAY_MODELS = (
    ("1min", models.BarData1Min),
    ("5min", models.BarData5Min),
    ("15min", models.BarData15Min),
    ("30min", models.BarData30Min),
    ("60min", models.BarData1H),
)

INTERDAY_MODELS = [
    (models.BarDataDaily, retrieve.daily_equity_data),
    (models.BarDataWeekly, retrieve.weekly_equity_data),
    (models.BarDataMonthly, retrieve.monthly_equity_data),
]

# fmt: off
SLICES = [
    "year1month1", "year1month2", "year1month3", "year1month4",
    "year1month5", "year1month6", "year1month7", "year1month8",
    "year1month9", "year1month10", "year1month11", "year1month12",
    "year2month1", "year2month2", "year2month3", "year2month4",
    "year2month5","year2month6", "year2month7", "year2month8",
    "year2month9", "year2month10", "year2month11", "year2month12",
]
# fmt: on


def _process_bar(symbol_id: int, timestamp, model, new_bar):
    try:
        model.objects.get(symbol_id=symbol_id, timestamp=timestamp)
    except ObjectDoesNotExist:
        model.objects.create(symbol_id=symbol_id, timestamp=timezone.now(), **new_bar)
        status = "Creating"
    else:
        model.objects.filter(symbol_id=symbol_id, timestamp=timestamp).update(**new_bar)
        status = "Updating"
    finally:
        log.debug(
            "%s %s entry for ID #: %s @ %s with values",
            status,
            model,
            symbol_id,
            timestamp,
        )


def interday_prices(symbol_id: int, symbol: str):
    for model, retrieve_func in INTERDAY_MODELS:
        (
            _process_bar(symbol_id, timestamp, model, new_bar)
            for timestamp, new_bar in retrieve_func(symbol)
        )


def intraday_prices(symbol_id: int, symbol: str):
    for interval, model in INTRADAY_MODELS:
        (
            _process_bar(symbol_id, timestamp, model, new_bar)
            for timestamp, new_bar in retrieve.intraday_equity_data_interval(
                symbol, interval
            )
        )


def intraday_extended_prices(symbol_id: int, symbol: str):
    for slice_ in SLICES:
        for interval, model in INTRADAY_MODELS:
            (
                _process_bar(symbol_id, timestamp, model, new_bar)
                for timestamp, new_bar in retrieve.intraday_equity_data_interval_extended(
                    symbol, interval, slice_
                )
            )
