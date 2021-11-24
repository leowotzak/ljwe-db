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
    output_size = "compact"
    data_type = "json"
    adjusted = True
    base_url = "https://www.alphavantage.co/query"
    database_url = os.environ.get("DATABASE_URL").replace(
        "postgres://", "postgresql://", 1
    )


class FullConfig:
    """Complete configuration

    Assumes case that user wants to pull as much data as possible
    from alpha vantage

    """

    api_key = os.environ.get("API_KEY")
    output_size = "full"
    data_type = "json"
    adjusted = True
    base_url = "https://www.alphavantage.co/query"
    database_url = os.environ.get("DATABASE_URL")
