from poloniex import Poloniex 

# Account key 
APIKEY = "PUT APIKEY HERE"
SECRET = "PUT SECRET HERE"

# Create poloniex object and initialize currency pair
polo = Poloniex(APIKEY, SECRET)
currency_pair = 'USDT_BTC'
depth = 50

# Get the data
pair_data = polo.returnOrderBook(currency_pair, depth)

asks_array = pair_data['asks']
bids_array = pair_data['bids']

# Test Print
print("\n\n", asks_array, "\n\n")
print(bids_array, "\n\n")
print(asks_array + bids_array, "\n\n")