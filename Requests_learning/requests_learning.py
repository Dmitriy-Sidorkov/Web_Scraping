import requests

params = dict(q='funny cats')
# Осуществляем запрос на сайт
response = requests.get('https://www.google.com/search', params=params)

# Комплексный ответ от сайта
print(response.status_code)
# Служебная информация которую передает сайт используемому браузеру
print(response.headers)
# Получаем HTML-код страницы в виде последовательности байт
print(response.content)
# Получаем HTML-код страницы в виде текста
print(response.text)
