from django.shortcuts import render
import requests


def get_weather_data(city):
    # city = request.GET.get('city')
    api_key = "5fe8e4e1d9aa825bc4d8e510080b070a"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)

    # Check if the response was successful
    if response.status_code == 200:
        weather_data = response.json()

        # Check if 'main' is in the response
        if 'main' in weather_data:
            return weather_data
        else:
            print("Error: 'main' key not found in the response.")
            print(weather_data)  # Print the full response for debugging
            return None
    else:
        print(f"Error: Received response with status code {response.status_code}")
        print(response.json())  # Print the full error message
        return None


# Usage
weather_data = get_weather_data('Lagos')
if weather_data:
    temperature = weather_data['main']['temp']
    weather_condition = weather_data['weather'][0]['description']
    print(f"Temperature: {temperature}°C")
    print(f"Weather Condition: {weather_condition}")
else:
    print("Failed to retrieve weather data.")
