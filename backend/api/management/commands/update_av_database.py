import logging
import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...updater import retrieve
from ...updater import update


logging.basicConfig(filename="main.log", filemode="a", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())


class Command(BaseCommand):
    help = "displays current time"

    def handle(self, *args, **kwargs):

        # TODO Improve argument handling (argparse)
        for symbol in retrieve.database_symbols():
            t = symbol.ticker
            update.interday_prices(symbol.symbol_id, t)
