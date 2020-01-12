import re
from collections import Counter
from twython import Twython
import json
from api_keys import key1, key2

keywords = input("Please enter your search keywords:\n")

# Request data from Twitter API using private keys (excluded for security):
twitter_api = Twython(key1, key2)

query = {
		'q': keywords,
		'result_type': 'top',
		'count': 100,
		'lang': 'en',
		}

data = ""

for status in twitter_api.search(**query)['statuses']:
	data += status['text']

# Clean up the raw data:
data = ''.join(data) # Create single string from file
data = re.sub(r'http\S+', '', data) # Remove hyperlinks
data = re.sub(r"\\[a-z][a-z]?[0-9]+", '', data) # Unicode
data = re.sub('[^A-Za-z ]+', '', data) # Remove special characters

# Place each clean word into a list for easier handling:
data_list = []

for each in data.split():
	data_list.append(each)

data_list = [word.lower() for word in data_list]

# Remove common words like 'the', 'you', 'this', etc (listed in stop_words.py), and convert to lowercase:
stop_words = open('stop_words.txt', 'r').read()
data_list = [word for word in data_list if word not in stop_words]

data_output = open( 'data.txt', 'w')

frequency = Counter(data_list)

# Save data to external file in format usable by AnyChart Javascript package:
for key, value in frequency.items() :
	if value > 2:
		data_output.write("{" + f'"x": "{key}", "value": {value}' + "},")

data_output.close()

# Data is now saved in data.txt and ready to be pasted into script.js - This really needs automated!