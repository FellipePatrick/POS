import requests
id = "1"
api_url = "http://127.0.0.1:5000"
response = requests.get(api_url+"/users/1")
print(response.json())