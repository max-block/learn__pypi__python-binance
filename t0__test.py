import os
from pprint import pprint

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()


client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
)

res = client.get_deposit_address(coin="SOL")
pprint(res)