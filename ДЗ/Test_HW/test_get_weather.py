import requests, json
url = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=5c62da02e9e30f91537def5669c10abc&units=metric&lang=uk')

def get_weather_from_api(data):
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    if url.status_code == 200:
        return {
            "temp": temp,
            "description": description
        }
    else:
        return url.status_code


def test_get_weather_from_api():
    weather_info = {"temp": 16.1, "description": 'рвані хмари'}

    assert get_weather_from_api(url.json()) == weather_info, 200

if __name__ == '__main__':
    test_get_weather_from_api()
    print("Всі тести пройдено успішно!")
