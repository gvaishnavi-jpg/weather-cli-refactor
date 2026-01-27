#!/usr/bin/env python3
"""Weather CLI - needs refactoring!"""

import requests
import json
import sys
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"
    r = requests.get(url)
    d = json.loads(r.text)
    
    print("\n=== Current Weather for " + city + " ===")
    print("Temperature: " + str(d['main']['temp']) + "°C")
    print("Feels like: " + str(d['main']['feels_like']) + "°C")
    print("Weather: " + d['weather'][0]['description'])
    print("Humidity: " + str(d['main']['humidity']) + "%")
    print("Wind Speed: " + str(d['wind']['speed']) + " m/s")
    print("Pressure: " + str(d['main']['pressure']) + " hPa")

def get_forecast(city):
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + API_KEY + "&units=metric"
    r = requests.get(url)
    d = json.loads(r.text)
    
    print("\n=== 5-Day Forecast for " + city + " ===")
    
    for item in d['list']:
        dt = datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        desc = item['weather'][0]['description']
        print(dt.strftime("%Y-%m-%d %H:%M") + " | " + str(temp) + "°C | " + desc)

def show_help():
    print("Weather CLI Tool")
    print("\nUsage:")
    print("  python weather.py current <city>")
    print("  python weather.py forecast <city>")
    print("\nExamples:")
    print("  python weather.py current London")
    print("  python weather.py forecast Tokyo")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "help":
        show_help()
        return
    
    if len(sys.argv) < 3:
        print("Error: Please provide a city name")
        return
    
    city = sys.argv[2]
    
    if command == "current":
        get_weather(city)
    elif command == "forecast":
        get_forecast(city)
    else:
        print("Error: Unknown command")
        show_help()

if __name__ == "__main__":
    main()
