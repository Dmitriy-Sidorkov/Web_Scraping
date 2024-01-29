import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Заводим переменную с личным api-токеном, значение токена берем на сайте
api_token = os.getenv('api_token')
# Инициализируем словарь с параметрами для Get запроса, смотрим список параметров в описании к API
params = dict(q='Moscow', appid=api_token, units='metric')

# Осуществляем подключение к API посредством запроса GET
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
# Выводим полученный дата-сет от API посредством форматирования JSON файла в словарь
print(response.json())
