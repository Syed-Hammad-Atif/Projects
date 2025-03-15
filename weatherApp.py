import requests

api_key = 'Your API Key'

print("Welcome to Weather App")

while True:
    user_input = input("Enter City: ")
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")

    if weather_data.json()['cod'] == '404':
        print("No City found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']

        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}°C")
    
    choice = input("\nDo you want to check another city? (y/n): ").lower()
    if choice != 'y':
        print("Exiting the weather app")
        break
