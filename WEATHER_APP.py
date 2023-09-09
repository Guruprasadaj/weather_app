import requests
import json
import time

# API Key from weatherapi.com (replace with your own key)
API_KEY = '221d643ebf8847798b9131652230609'

# Constants for API URLs
BASE_URL = 'https://api.weatherapi.com/v1/'
WEATHER_ENDPOINT = 'current.json'
SEARCH_ENDPOINT = 'search.json'
FAVORITES_FILE = 'favorites.txt'

# Function to make API requests
def fetch_weather_data(city):
    params = {'key': API_KEY, 'q': city}
    response = requests.get(BASE_URL + WEATHER_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data for {city}")
        return None

# Function to search for cities
def search_city(query):
    params = {'key': API_KEY, 'q': query}
    response = requests.get(BASE_URL + SEARCH_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to perform city search.")
        return None

# Function to display weather information
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['location']['name']}, {weather_data['location']['region']}, {weather_data['location']['country']}:")
        print(f"Condition: {weather_data['current']['condition']['text']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Feels Like: {weather_data['current']['feelslike_c']}°C")
        print(f"Wind Speed: {weather_data['current']['wind_kph']} km/h")
    else:
        print("No weather data available.")

# Function to add a city to favorites
def add_to_favorites(city):
    with open(FAVORITES_FILE, 'a') as file:
        file.write(city + '\n')
    print(f"{city} added to favorites.")

# Function to list favorite cities
def list_favorites():
    try:
        with open(FAVORITES_FILE, 'r') as file:
            favorites = file.read().splitlines()
            if favorites:
                print("Favorite Cities:")
                for i, city in enumerate(favorites, 1):
                    print(f"{i}. {city}")
            else:
                print("No favorite cities found.")
    except FileNotFoundError:
        print("No favorite cities found.")

# Main program
if __name__ == '__main__':
    while True:
        print("\nWeather Checking Application Menu:")
        print("1. Check Weather by City")
        print("2. Search City")
        print("3. Add City to Favorites")
        print("4. List Favorite Cities")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            weather_data = fetch_weather_data(city)
            display_weather(weather_data)
        elif choice == '2':
            query = input("Enter city name or keyword: ")
            search_results = search_city(query)
            if search_results:
                for i, result in enumerate(search_results, 1):
                    print(f"{i}. {result['name']}, {result['region']}, {result['country']}")
            else:
                print("No results found.")
        elif choice == '3':
            city = input("Enter city name to add to favorites: ")
            add_to_favorites(city)
        elif choice == '4':
            list_favorites()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(15)  # Auto-refresh every 15 seconds
