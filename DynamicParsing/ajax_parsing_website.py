from requests import Session
from bs4 import BeautifulSoup

# url = 'https://scrapingclub.com/exercise/ajaxdetail/'
# response = requests.get(url).json()
# for key in response.keys():
#     print(f'{key} --> {response[key]}')

base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}


def main(base_url):
    s = Session()
    s.headers.update(headers)

    count_page = 1
    while True:
        if count_page > 1:
            url = base_url + f'?page={count_page}'
        else:
            url = base_url
        response = s.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        if count_page == 1:
            pagination = int(soup.find('nav', class_='pagination').find_all('span', class_='page')[-2].text)

        products = soup.find_all('div', class_='w-full rounded border post')
        for product in products:
            name = product.find('h4').text.strip()
            price = product.find('h5').text
            print(name, price, sep='\n', end='\n\n')

        if count_page == pagination:
            break

        count_page += 1


if __name__ == '__main__':
    main(base_url)
