import requests, json
url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&appid=5c62da02e9e30f91537def5669c10abc&units=metric&lang=uk')

def get_weather_from_api(data):

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return {
        "temp": temp,
        "description": description
    }, url.status_code

print(get_weather_from_api(url.json()))
