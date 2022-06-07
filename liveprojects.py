import requests
from pprint import pprint

# github username
username = "DevArv"
# url to request
url = f"https://api.github.com/users/DevArv"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)