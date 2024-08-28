from django.shortcuts import render
import requests
from django.conf import settings


def get_weather_data(city):
    api_key = settings.OPENWEATHER_API_KEY
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)

    if response.status_code == 200:
        weather_data = response.json()
        if 'main' in weather_data:
            return weather_data
        else:
            print("Error: 'main' key not found in the response.")
            print(weather_data)
            return None
    else:
        print(f"Error: Received response with status code {response.status_code}")
        print(response.json())
        return None


def weather_view(request):
    city = request.GET.get('city', 'Lagos')  # Default to Lagos if no city is provided
    weather_data = get_weather_data(city)

    if weather_data:
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'weather_condition': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        context = {
            'error': "Failed to retrieve weather data. Please try again later."
        }

    return render(request, 'weather.html', context)
