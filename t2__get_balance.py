import os

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

proxies = {"http": os.getenv("PROXY"), "https": os.getenv("PROXY")}

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    requests_params={"proxies": proxies},
)

res = client.get_asset_balance(asset="SOL")
print(res)
# {'asset': 'SOL', 'free': '0.00000000', 'locked': '0.00000000'}
