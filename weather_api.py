import requests

params = {
  'access_key': 'e224f6174e3bae9aa0560ee5d8d90dd1',
  'query': 'New York'
}

api_result = requests.get('https://api.weatherstack.com/current', params)

api_response = api_result.json()

print(api_response)