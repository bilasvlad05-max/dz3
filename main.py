import requests

url = "https://api.open-meteo.com/v1/forecast"

latitude = 49.8397
longitude = 24.0297

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
weather = response.json()

temperature = weather["current"]["temperature_2m"]
humidity = weather["current"]["relative_humidity_2m"]
wind = weather["current"]["wind_speed_10m"]

print(" ПОГОДА У ЛЬВОВІ")
print(f"Температура: {temperature} °C")
print(f" Вологість: {humidity} %")
print(f"Вітер: {wind} км/год")