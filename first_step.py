import requests
from bs4 import BeautifulSoup
from time import sleep


def response(url_site_response, user_agent_response, filter_value):
    """Функция сбора требуемого HTML-кода страницы для последующего анализа элементов"""
    response_site = requests.get(url_site_response,
                                 headers=user_agent_response)  # Осуществляем запрос на сайт и получаем HTML-код страницы
    soup = BeautifulSoup(response_site.text, features='lxml')  # Осуществляем разбор HTML-кода при помощи парсера
    data = soup.find_all('div', class_=filter_value)  # Осуществляем фильтрацию по необходимому тегу
    return data  # Возвращаем список отфильтрованного HTML-кода


user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
}  # Необходимо чтобы не получить блокировку сайта на подозрительный запрос
list_card_url = []
def card_url():


for page_number in range(1, 8):  # Запускаем цикл в соответствии с кол-вом страниц с которых требуется получить HTML-код
    sleep(3)  # Необходимо чтобы не получить блокировку сайта на подозрительный запрос
    url_site = f'https://scrapingclub.com/exercise/list_basic/?page={page_number}'
    for card in response(url_site, user_agent, filter_value="w-full rounded border"):
        list_card_url.append('https://scrapingclub.com' + card.find('a').get('href'))
    # print(*list_card_url, sep='\n')
for card_url in list_card_url:
    data_card = response(card_url, user_agent, filter_value='my-8 w-full rounded border')
    for elem in data_card:
        name_product = elem.find('h3').text.strip()
        price_product = elem.find('h4').text.strip()
        description_product = elem.find('p').text.strip()
        url_img_product = 'https://scrapingclub.com' + elem.find('img').get('src')
        print(name_product, price_product, description_product, url_img_product, sep='\n', end='\n\n')
    # print(name, price, url_img, sep='\n', end='\n\n')
