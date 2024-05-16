import requests
import sys

API_KEY = 'enter_ your_API_key'  # Replace with your OpenWeatherMap API key

def get_weather(location):
    # Construct the API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        # Extract the needed information
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        conditions = weather_data['weather'][0]['description']
        
        # Print the weather information
        print(f"Current weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions.capitalize()}")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city_name>")
        sys.exit(1)
    
    location = sys.argv[1]
    get_weather(location)

if __name__ == "__main__":
    main()
