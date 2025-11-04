#Requests is one of the popular packages in python
# to make http requests

#This is for pretty printing json responses
import json

import requests
import sys

if(len(sys.argv) != 2):
    sys.exit()

#argument passed is weezer for eg
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv[1])

print(json.dumps(response.json(), indent = 2))