import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    api_key = os.environ.get("API_KEY")
    output_size = "compact"  # or full
    data_type = "json"  # or csv
    adjusted = False
    base_url = "https://www.alphavantage.co/query"
    database_url = os.environ.get("DATABASE_URL")
