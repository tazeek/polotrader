from urllib.request import urlopen, Request

import json
import time
import hmac
import hashlib

# Function for creating timestamp
def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):

	return time.mktime(time.strptime(datestr, format))


class Poloniex:

	# For own accounts (non-public)
	def __init__(self, APIKey, Secret):
		
		self.APIKey = APIKey
		self.Secret = Secret

	def post_process(self, before):

		after = before

		# Add timestamps if there isn't one but is a datetime
		if('return' in after and (isinstance(after['return'], list))):
				
				for x in xrange(0, len(after['return'])):

					if(isinstance(after['return'][x], dict) and 'datetime' in after['return'][x] and 'timestamp' not in after['return'][x]):
						after['return'][x]['timestamp'] = float(createTimeStamp(after['return'][x]['datetime']))

		return after

	# API Querying
	def apiQuery(self, command, req={}, depth=50):

		poloniex_url = 'https://poloniex.com/public?command='
		currency_pair = str(req['currencyPair'])

		if(command == "returnTicker" or command == "return24Volume"):
			ret = urlopen(Request(poloniex_url + command))
			return json.loads(ret.read())
		elif(command == "returnOrderBook"):
			ret = urlopen(Request(poloniex_url + command + '&currencyPair=' + currency_pair + '&depth=' + str(depth)))
			return json.loads(ret.read())
		elif(command == "returnMarketTradeHistory"):
			ret = urlopen(Request(poloniex_url + "returnTradeHistory" + '&currencyPair=' + currency_pair))
			return json.loads(ret.read())
		else:

			req['command'] = command
			req['nonce'] = int(time.time()*1000)
			post_data = urllib.urlencode(req)

			sign = hmac.new(self.Secret, post_data, hashlib.sha512).hexdigest()

			headers = {'Sign': sign, 'Key': self.APIKey}

			ret = urlopen(Request('https://poloniex.com/tradingApi', post_data, headers))
			jsonRet = json.loads(ret.read())
			return self.post_process(jsonRet)

	def returnTicker(self):
		return self.apiQuery("returnTicker")

	def return24Volume(self):
		return self.apiQuery("return24Volume")

	def returnOrderBook (self, currency_pair, depth):
		return self.apiQuery("returnOrderBook", {'currencyPair': currency_pair}, depth)

	def returnMarketTradeHistory (self, currency_pair):
		return self.apiQuery("returnMarketTradeHistory", {'currencyPair': currency_pair})




'''
https://pastebin.com/8fBVpjaj
https://github.com/owocki/pytrader/blob/master/history/poloniex.py
https://poloniex.com/support/api/
https://poloniexapi.wordpress.com/
https://github.com/s4w3d0ff/python-poloniex
'''