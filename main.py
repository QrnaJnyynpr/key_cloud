from flask import Flask, render_template, request, url_for
import re
from collections import Counter
from twython import Twython
from keys import key1, key2

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/')
def sender():
	keyword = request.args.get('keyword') #Fetch keywords from index.html

	# Request data from Twitter API with proper authentication:
	twitter_api = Twython(key1, key2)

	query = {'q': keyword,
			'result_type': 'top',
			'count': 100,
			'lang': 'en',
			}

	data = ""

	for status in twitter_api.search(**query)['statuses']:
		data += status['text']

	# Cleaning up the raw data:
	data = ''.join(data) # Create single string from file
	data = re.sub(r'http\S+', '', data) # Remove hyperlinks
	data = re.sub(r"\\[a-z][a-z]?[0-9]+", '', data) # Remove unicode
	data = re.sub('[^A-Za-z ]+', '', data) # Remove special characters

	# Place each clean word into a list for easier handling:
	data_list = []

	for each in data.split():
		data_list.append(each)

	data_list = [word.lower() for word in data_list]

	# Remove common words like 'the', 'you', 'this', etc:
	stop_words = open('stop_words.txt', 'r').read()
	data_list = [word for word in data_list if word not in stop_words]

	data_output = ""

	# Organise repeated words by count value and sort:
	frequency = Counter(data_list)

	# Save data as string with Javascript dictionary format:
	for key, value in frequency.items() :
		if value > 1:
			string_output = '{"x": "' + key + '", "value": ' + str(value) + '}, '
			data_output += string_output
	data_output = data_output[:-2] #Removes trailing comma from string
	return render_template('result.html', data_output=data_output, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)