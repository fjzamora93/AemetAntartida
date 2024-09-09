#!/usr/bin/env python
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import pprint

# Define the URL
url = 'http://demo.ckan.org/api/3/action/group_list'

# Define the headers for the request
headers = {
    'Authorization': 'your-api-key'
}

# Make the HTTP request.
request = Request(url, headers=headers)

# Make the HTTP request.
response = urlopen(url)
assert response.status == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read().decode('utf-8'))

# Check the contents of the response.
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)