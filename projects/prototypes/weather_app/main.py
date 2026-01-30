import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather = response.json()

        print(f"Weather in {weather['nearest_area'][0]['areaName'][0]['value']}:")
        print(f"  Condition: {weather['current_condition'][0]['weatherDesc'][0]['value']}")
        print(f"  Temperature: {weather['current_condition'][0]['temp_C']}°C")
        print(f"  Humidity: {weather['current_condition'][0]['humidity']}%")
        print(f"  Wind: {weather['current_condition'][0]['windspeedKmph']} km/h")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
