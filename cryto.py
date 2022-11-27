import api
from binance.client import Client
from binance.enums import *

client = Client(api.API_Key,  api.Secret_Key, tld='com')
list_of_tickers = client.get_all_tickers()
print(list_of_tickers)