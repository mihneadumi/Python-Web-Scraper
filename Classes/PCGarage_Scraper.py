from Classes.Product_Class import Product
from bs4 import BeautifulSoup
from selenium import webdriver

class PCGarage_Scraper:
    def __init__(self, pcgarage_link: str):
        self.name = 'PCGarage'
        self.page_nr = 1
        self.pcgarage_link = pcgarage_link
        self.raw_product_list = self.get_raw_product_list(pcgarage_link)
        self.product_list = self.get_product_list(self.raw_product_list)
    
    def get_page_raw_product_list(self, pcgarage_link: str) -> list:
        url = pcgarage_link
        driver = webdriver.Edge()
        driver.get(url)
        # time.sleep(5)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        raw_page_product_list = soup.find_all('div', {'class': 'product_box'})
        return raw_page_product_list

    def get_raw_product_list(self, pcgarage_link: str) -> list:
        raw_product_list = []
        next_page_link = pcgarage_link
        while next_page_link:
            print(f'Getting products from page {self.page_nr}')
            self.page_nr += 1
            raw_product_list.extend(self.get_page_raw_product_list(next_page_link))
            next_page_link = self.get_next_page_link(next_page_link)
        return raw_product_list
    
    def get_product_list(self, raw_product_list: list) -> list:
        product_list = []
        for product in raw_product_list:
            # name and link located in the same tag
            data = product.find('h2', {'class': 'my-0'}).find('a')
            name = data.get('title').strip()
            link = data.get('href')
            price = float(product.find('p', {'class': 'price'}).text.replace(' RON', '').replace(' ', '').replace('.', '').replace(',', '.'))
            product_list.append(Product(name, price, None, link))
        return product_list
    
    def get_next_page_link(self, pcgarage_link: str) -> str:
        url = pcgarage_link
        driver = webdriver.Edge()
        driver.get(url)
        # time.sleep(5)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        next_page_link = soup.find('a', {'aria-label': 'Pagina urmatoare'})
        if next_page_link:
            next_page_link = next_page_link.get('href')
        return next_page_link