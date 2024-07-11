import requests
from datetime import datetime

def get_weather_data(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0adbc2aaa39fabdbf15254f0fd0cad4f').json()
    #print(response)
    # print('\n')
    # print('list')
    return response

def get_current_weather(response):
    current_weather = response['main']
    temperature = int(current_weather['temp'] - 273.15)
    humidity = current_weather['humidity']
    pressure = current_weather['pressure']
    wind_speed = response['wind']['speed']
    return f'Температура: {temperature} °C\nВлажность: {humidity}%\nДавление: {pressure} hPa\nСкорость ветра: {wind_speed} м/с'

def get_forecast(response):
    forecast = response['weather'][0]
    description = forecast['description']
    timeSec = response['dt']
    
    date =  datetime.fromtimestamp(timeSec)
    return f'Дата: {date} \nОписание погоды: {description}'
    #return f'Дата: {date.strftime("%Y-%m-%d")}'

city = input('Введите название города: ')
response = get_weather_data(city)
current_weather = get_current_weather(response)
forecast = get_forecast(response)

print(f'Прогноз погоды для {city}:')
print(current_weather)
print(forecast)