import requests
from bs4 import BeautifulSoup
from time import sleep

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
}  # Необходимо чтобы не получить блокировку сайта на подозрительный запрос


def response(url_site_response, user_agent_response, filter_value):
    """Функция сбора требуемого HTML-кода страницы для последующего анализа элементов"""
    response_site = requests.get(url_site_response,
                                 headers=user_agent_response)  # Осуществляем запрос на сайт и получаем HTML-код страницы
    soup = BeautifulSoup(response_site.text, features='lxml')  # Осуществляем разбор HTML-кода при помощи парсера
    data = soup.find_all('div', class_=filter_value)  # Осуществляем фильтрацию по необходимому тегу
    return data  # Возвращаем список отфильтрованного HTML-кода


def get_url_page_product():
    for page_number in range(1, 8):  # Запускаем цикл в соответствии с кол-вом страниц с которых требуется получить HTML-код
        url_site = f'https://scrapingclub.com/exercise/list_basic/?page={page_number}'
        for data_page in response(url_site, user_agent, filter_value="w-full rounded border"):  # Запускаем цикл по списку отфильтрованного HTML-кода с товарами
            url_page_product = 'https://scrapingclub.com' + data_page.find('a').get('href')  # Получаем url адрес на страницу конкретного товара
            yield url_page_product


def get_info_product():
    for url_page_product in get_url_page_product():
        # sleep(3)  # Необходимо чтобы не получить блокировку сайта на подозрительный запрос
        for data_product in response(url_page_product, user_agent, filter_value='my-8 w-full rounded border'):  # Запускаем цикл по списку отфильтрованного HTML-кода со страницы конкретного товара
            name_product = data_product.find('h3').text.strip()
            price_product = data_product.find('h4').text.strip()
            description_product = data_product.find('p').text.strip()
            url_img_product = 'https://scrapingclub.com' + data_product.find('img').get('src')
            yield name_product, price_product, description_product, url_img_product
