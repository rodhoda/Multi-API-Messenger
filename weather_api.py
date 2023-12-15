import requests

params = {
  'access_key': 'e224f6174e3bae9aa0560ee5d8d90dd1',
  'query': 'New York'
}
api_key = 'c8f638f609690847cebb4208509862a1'
lat = 47.697109
long = -122.025803
api_result = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&unit=metric&appid={api_key}')

api_response = api_result.json()

kelvin_to_celsius = 272.15

def weather_api():
    current_temp = round(int(api_response['current']['temp']) - kelvin_to_celsius)
    daily_weather = api_response['daily'][0]['summary']
    max_daily_temp = round(int(api_response['daily'][0]['temp']['max']) - kelvin_to_celsius)
    min_daily_temp = round(int(api_response['daily'][0]['temp']['min']) - kelvin_to_celsius)
    daily_weather = [f"{str(current_temp)}\u00B0",f"{str(max_daily_temp)}\u00B0", f"{str(min_daily_temp)}\u00B0",
                     daily_weather]
    return daily_weather