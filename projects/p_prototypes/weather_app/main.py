import requests
import sys

def main():
    """
    Fetches and displays weather information for a specified city using the wttr.in service.
    """
    # Check if a city name was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    # wttr.in endpoint with format=j1 returns detailed JSON data
    url = f"https://wttr.in/{city}?format=j1"

    try:
        # Send GET request to the weather service
        response = requests.get(url)
        # Raise exception for HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()

        # Extract relevant fields from the nested JSON structure
        area_name = weather_data['nearest_area'][0]['areaName'][0]['value']
        condition = weather_data['current_condition'][0]['weatherDesc'][0]['value']
        temp_c = weather_data['current_condition'][0]['temp_C']
        humidity = weather_data['current_condition'][0]['humidity']
        wind_speed = weather_data['current_condition'][0]['windspeedKmph']

        # Display the formatted weather report
        print(f"Weather in {area_name}:")
        print(f"  Condition: {condition}")
        print(f"  Temperature: {temp_c}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} km/h")

    except requests.exceptions.RequestException as e:
        # Handle connection issues or invalid requests
        print(f"Request Error: {e}")
        sys.exit(1)
    except (KeyError, IndexError) as e:
        # Handle cases where the JSON structure is not as expected (e.g., city not found)
        print(f"Data Parsing Error: Could not find weather data for '{city}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()