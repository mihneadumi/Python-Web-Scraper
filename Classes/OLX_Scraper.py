from Classes.Product_Class import Product
from bs4 import BeautifulSoup
import requests


class OLX_Scraper:
    
        def __init__(self, olx_link: str) -> None:
            self.name = 'OLX'
            self.page_nr = 1
            self.olx_link = olx_link
            self.raw_product_list = self.get_raw_product_list(olx_link)
            self.product_list = self.get_product_list(self.raw_product_list)    
    
        def get_page_raw_product_list(self, olx_link: str) -> list:
            url = olx_link
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            raw_page_product_list = soup.find_all('a', {'class': 'css-rc5s2u'})
            return raw_page_product_list
    
        def get_raw_product_list(self, olx_link: str) -> list:
            raw_product_list = []
            next_page_link = olx_link
            while next_page_link:
                print(f'Getting products from page {self.page_nr}')
                self.page_nr += 1
                raw_product_list.extend(self.get_page_raw_product_list(next_page_link))
                next_page_link = self.get_next_page_link(next_page_link)
            return raw_product_list
    
        def get_product_list(self, raw_product_list: list) -> list:
            product_list = []
            for product in raw_product_list:
                name = product.find('h6', {'class': 'css-16v5mdi er34gjf0'}).text.strip()
                price = float(product.find('p', {'data-testid': 'ad-price'}).text.replace('€', '').replace('Prețul e negociabil', '').replace(' ', '').replace(',', '.'))
                link = product.get('href')
                product_list.append(Product(name, price, None, link))
            return product_list
    
        def get_next_page_link(self, olx_link: str) -> str:
            url = olx_link
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            next_page_link = soup.find('a', {'data-testid': 'pagination-forward'})
            if next_page_link:
                next_page_link ='https://www.olx.ro/' + next_page_link.get('href')
            return next_page_link