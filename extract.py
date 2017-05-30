from poloniex import Poloniex 

import pandas as pd

# Account key 
APIKEY = "PUT APIKEY HERE"
SECRET = "PUT SECRET HERE"

# Create poloniex object and initialize currency pair
polo = Poloniex(APIKEY, SECRET)
currency_pair = 'USDT_BTC'
depth = 20000

# Get the data
pair_data = polo.returnOrderBook(currency_pair, depth)

asks_array = pair_data['asks']
bids_array = pair_data['bids']

# Create dataframe from 'asks' data
asks_df = pd.DataFrame(asks_array, columns=['askRate', 'askAmount'])
asks_df['askRate'] = asks_df['askRate'].apply(pd.to_numeric)
asks_df['Product'] = asks_df['askRate'] * asks_df['askAmount']

# Create dataframe from 'bids' data
bids_df = pd.DataFrame(bids_array, columns = ['bidRate', 'bidAmount'])
bids_df['bidRate'] = bids_df['bidRate'].apply(pd.to_numeric)
bids_df['Product'] = bids_df['bidRate'] * bids_df['bidAmount']

# Aggregation of 'Rate' column
total_ask_product = asks_df['Product'].sum() 
total_bid_product = bids_df['Product'].sum()

# Test Print
print(total_ask_product,"\n")
print(total_bid_product, "\n")