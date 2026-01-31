import requests

# API key (replace with your own)
API_KEY = "30a5c0d4279c6b446b162e4c5127e9f5"

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# User input
city = input("Enter city name: ")

# Parameters
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

# API request
response = requests.get(BASE_URL, params=params)

# Convert response to JSON
data = response.json()

# Check if city is found
if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]

    print("\nWeather Information")
    print("-------------------")
    print(f"City        : {city}")
    print(f"Temperature : {temperature} °C")
    print(f"Humidity    : {humidity} %")
    print(f"Condition   : {weather_desc}")
else:
    print("City not found!")

