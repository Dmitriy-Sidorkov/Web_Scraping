from requests import Session
from bs4 import BeautifulSoup

# Идентификационная строка клиентского приложения, необходимо чтобы не получить блокировку сайта
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'}
# Инициализируем словарь для осуществления POST запроса
login_dict = dict(csrf_token=None, username='one', password='love')

work = Session()
# Осуществляем вход на главную страницу сайта
work.get('https://quotes.toscrape.com/', headers=user_agent)
# Осуществляем вход на страницу авторизации сайта
response = work.get('https://quotes.toscrape.com/login', headers=user_agent)
# Осуществляем разбор HTML-кода при помощи парсера
soup = BeautifulSoup(response.text, 'lxml')
# Осуществляем фильтрацию кода для поиска значения необходимого атрибута
token_website = soup.find('form').find('input').get('value')
# Осуществляем обновление словаря для POST запроса
login_dict['csrf_token'] = token_website

# Осуществляем запрос POST с передачей требуемого словаря
result = work.post('https://quotes.toscrape.com/login', headers=user_agent, data=login_dict, allow_redirects=True)
print(result.text)
