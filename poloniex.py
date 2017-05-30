from urllib.request import urlopen

import json
import time
import hmac
import hashlib

# Function for creating timestamp
def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):

	return time.mktime(time.strptime(datestr, format))