import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from Classes.Product_Class import Product

class Altex_Scraper():
    def __init__(self, altex_link: str) -> None:
        self.name = 'Altex'
        raw_product_list = self.get_raw_product_list(altex_link)
        self.product_list = self.get_product_list(raw_product_list)
    
    def get_page_raw_product_list(self, altex_link: str) -> list:
        # scrape the link using Selenium
        url = altex_link
        driver = webdriver.Edge()
        driver.get(url)
        # time.sleep(5)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        raw_page_product_list = soup.find('ul', {'class': 'Products flex flex-wrap relative -mx-1 sm:-mx-2'})
        raw_page_product_list = raw_page_product_list.find_all('a', {'class': 'Product flex flex-col relative hover:shadow-mixRedYellow'})

        return raw_page_product_list
        
    
    def get_raw_product_list(self, altex_link: str) -> list:
        raw_product_list = []
        next_page_link = altex_link
        while next_page_link:
            raw_product_list.extend(self.get_page_raw_product_list(next_page_link))
            next_page_link = self.get_next_page_link(next_page_link)
        return raw_product_list
    
    def get_product_list(self, raw_product_list: list) -> list:
        product_list = []
        for product in raw_product_list:
            name = product.find('h2', {'class': 'Product-name Heading leading-20 text-sm truncate-3-lines min-h-60px'}).text.strip()
            prices = product.find_all('span', {'class': 'Price-int leading-none'})
            if len(prices) == 2:
                price = float(prices[1].text.strip().replace('.', '').replace(',', '.'))
                full_price = float(prices[0].text.strip().replace('.', '').replace(',', '.'))
            else:
                price = float(prices[0].text.strip().replace('.', '').replace(',', '.'))
                full_price = price

            link = "https://altex.ro/" + product.get('href')
            product_list.append(Product(name, price, full_price, link))
        return product_list
    
    def get_next_page_link(self, altex_link: str) -> str:
        url = altex_link
        driver = webdriver.Edge(headLess=True)
        driver.get(url)
        # time.sleep(5)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        next_page_link = soup.find('a', {'class': 'inline-block py-1 px-2 mx-0.5 sm:mx-1 text-sm border border-gray-1100 rounded-md items-center text-center bg-white'})
        if next_page_link:
            content = next_page_link.find('div', {'class': 'hidden md:inline-block'}).text.strip()
            if content == 'Pagina urmatoare':
                next_page_link = next_page_link.get('href')
            else:
                next_page_link = None
        else:
            next_page_link = None
        return next_page_link