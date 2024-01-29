import requests
from bs4 import BeautifulSoup
from time import sleep

# Идентификационная строка клиентского приложения, необходимо чтобы не получить блокировку сайта
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'}


def response(url_site_response, user_agent_response, filter_value):
    """Функция сбора требуемого HTML-кода страницы для последующего анализа элементов"""
    # Осуществляем запрос на сайт и получаем HTML-код страницы
    response_site = requests.get(url_site_response, headers=user_agent_response)
    # Осуществляем разбор HTML-кода при помощи парсера
    soup = BeautifulSoup(response_site.text, features='lxml')
    # Осуществляем фильтрацию по необходимому тегу
    data = soup.find_all('div', class_=filter_value)
    return data  # Возвращаем список отфильтрованного HTML-кода


def get_url_page_product():
    """Функция сбора ссылок на страницу каждого товара"""
    # Запускаем цикл в соответствии с кол-вом страниц с которых требуется получить HTML-код
    for page_number in range(1, 7):
        url_site = f'https://scrapingclub.com/exercise/list_basic/?page={page_number}'
        # Запускаем цикл по списку отфильтрованного HTML-кода с товарами
        for data_page in response(url_site, user_agent, filter_value="w-full rounded border"):
            # Получаем url адрес на страницу конкретного товара
            url_page_product = 'https://scrapingclub.com' + data_page.find('a').get('href')
            yield url_page_product


def download_image_product(url_image, user_agent_response, name_product):
    """Функция загрузки изображения товара с сайта"""
    # Осуществляем запрос на сайт и подгружаем изображение
    resp = requests.get(url_image, headers=user_agent_response, stream=True)
    # Создаем файл с изображением
    with open('image_product\\' + name_product + '_' + url_image.split('/')[-1], "wb") as file:
        #
        for image_product in resp.iter_content(1024 * 1024):
            # Осуществляем запись изображения в файл
            file.write(image_product)


def get_info_product():
    """Функция сбора требуемой информации по товару"""
    for url_page_product in get_url_page_product():
        # Необходимо чтобы не получить блокировку сайта на подозрительный запрос
        sleep(3)
        # Запускаем цикл по списку отфильтрованного HTML-кода со страницы конкретного товара
        for data_product in response(url_page_product, user_agent, filter_value='my-8 w-full rounded border'):
            # Заводим переменные в соответствии с искомой информацией
            name_product = data_product.find('h3').text.strip()
            price_product = data_product.find('h4').text.strip()
            description_product = data_product.find('p').text.strip()
            url_img_product = 'https://scrapingclub.com' + data_product.find('img').get('src')
            # Осуществляем загрузку изображения товара на локальную машину
            download_image_product(url_img_product, user_agent, name_product)
            yield name_product, price_product, description_product, url_img_product
