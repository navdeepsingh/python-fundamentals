import requests

api_url = 'https://shibe.online/api/shibes'

response = requests.get(api_url, params={'count': 10})

response_json = response.json()
print(f"Status Code: {response.status_code}, Response: {response_json}")