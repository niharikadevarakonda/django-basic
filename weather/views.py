import os
import requests
from django.shortcuts import render


def weather(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = os.environ.get('OPENWEATHER_API_KEY')

        url = 'https://api.openweathermap.org/data/2.5/weather'

        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(url, params=params)
        data = response.json()
        
        
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        else:
            weather_data = {
                'error': data.get('message', 'Something went wrong')
            }

    return render(request, 'weather.html', {'weather': weather_data})
