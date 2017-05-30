from poloniex import Poloniex 

# Account key 
APIKEY = "PUT APIKEY HERE"
SECRET = "PUT SECRET HERE"

# Create poloniex object and initialize currency pair
polo = Poloniex(APIKEY, SECRET)
currency_pair = 'USDT_BTC'
depth = 10000

# Get the data
pair_data = polo.returnOrderBook(currency_pair, depth)

asks_array = pair_data['asks']
bids_array = pair_data['bids']

# Test Print
print(len(asks_array))
print(len(bids_array))