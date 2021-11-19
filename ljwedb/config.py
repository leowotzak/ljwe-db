"""Collection of configuration files for ease of use, debugging, & testing


"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Typical configuration

    Assumes case that user wants to simply update with recent data

    """
    api_key = os.environ.get("API_KEY")
class FullConfig:
    """Complete configuration

    Assumes case that user wants to pull as much data as possible
    from alpha vantage

    """
    adjusted = True
    base_url = "https://www.alphavantage.co/query"
    database_url = os.environ.get("DATABASE_URL")
