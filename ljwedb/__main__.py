"""Adds/updates price data for each symbol in symbols table"""

import logging
import time

logging.basicConfig(filename="main.log", filemode="a", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

from .update import update
from .retrieve import retrieve

PER_REQUEST_WAIT = 15

symbols = []
# ? how to run without any input and do nothing
# if not symbols:
#     symbols = []

for symbol_id, bar_data in retrieve.database_symbols(symbols):
    t = bar_data["ticker"]
    update.daily_prices(t, symbol_id)
    time.sleep(PER_REQUEST_WAIT)
    update.weekly_prices(t, symbol_id)
    time.sleep(PER_REQUEST_WAIT)
    update.monthly_prices(t, symbol_id)
    time.sleep(PER_REQUEST_WAIT)
    update.intraday_extended_history_prices(t, symbol_id)
