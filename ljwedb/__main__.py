"""Adds/updates price data for each symbol in symbols table"""

import logging
import time

from . import retrieve, update

logging.basicConfig(filename="main.log", filemode="a", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

PER_REQUEST_WAIT = 15

symbols = []
# ? how to run without any input and do nothing
# if not symbols:
#     symbols = []

retrieve.wiki_sp500()


# for symbol_id, bar_data in retrieve.database_symbols(symbols):
#     update.daily_prices(bar_data["ticker"], symbol_id)
#     time.sleep(PER_REQUEST_WAIT)
