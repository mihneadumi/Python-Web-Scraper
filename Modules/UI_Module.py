import os

from Classes.PCGarage_Scraper import PCGarage_Scraper
from Classes.OLX_Scraper import OLX_Scraper
from Classes.KSA_Scraper import KSA_Scraper
from Classes.Altex_Scraper import Altex_Scraper

from Modules.Repository_Module import Repo


class UI:
    def __init__(self) -> None:
        self.scraper = None
        self.get_scraper()
        self.repo = Repo(self.scraper.product_list)
        self.start_app()

    def get_scraper(self):
        """
        Gets the scraper depending on the website domain
        """
        os.system('cls')
        self.scraper = None
        while self.scraper is None:
            link = input('Enter the link to the page with the products or "exit" to close: \n> ')
            if 'ksaretail' in link:
                self.scraper = KSA_Scraper(link)
            elif 'altex.ro' in link:
                try: # The scraper doesn't work for certain pages because of the website's structure
                    self.scraper = Altex_Scraper(link)
                except Exception as e:
                    print(e)
            elif 'olx.ro' in link:
                self.scraper = OLX_Scraper(link)
            elif 'pcgarage.ro' in link:
                try:
                    self.scraper = PCGarage_Scraper(link)
                except Exception as e:
                    print("Couldn't scrape the link. Make sure it's a link to a product page")
            elif link == 'exit':
                exit()
            else:
                os.system('cls')
                print('No scraper for this site yet')

    def start_app(self):
        """
        Main menu of the app
        """
        while True:
            # os.system('cls')
            self.print_product_list()
            print('\n---------------------Menu---------------------\n')
            print('Currently scraping: ' + self.scraper.name)
            print('1. Sort the product list')
            print('2. Filter the product list')
            print('3. Remove filters')
            print('4. Scrape a different link')
            print('5. Export list to excel')
            print('6. Export list to csv')
            print('0. Exit')
            choice = input('> ')
            if choice == '1':
                os.system('cls')
                print('---------------------Sort Menu---------------------')
                print('1. Sort by name')
                print('2. Sort by price')
                print('3. Sort by discount')
                print('0. Back')
                choice = input('> ')
                if choice == '1':
                    self.repo.sort_by_name()
                elif choice == '2':
                    self.repo.sort_by_price()
                elif choice == '3':
                    self.repo.sort_by_discount()
                elif choice == '0':
                    continue
                else:
                    print('Invalid choice')
            elif choice == '2':
                os.system('cls')
                print('---------------------Filter Menu---------------------')
                print('1. Filter by name')
                print('2. Filter by price')
                print('3. Filter by discount')
                print('4. Filter by price range')
                print('5. Filter by discount range')
                print('0. Back')
                choice = input('> ')
                if choice == '1':
                    name = input('Enter the name: \n> ')
                    self.repo.product_list = self.repo.filter_by_name(name)
                elif choice == '2':
                    price = float(input('Enter the price: \n> '))
                    self.repo.product_list = self.repo.filter_by_price(price)
                elif choice == '3':
                    discount = int(input('Enter the discount: \n> '))
                    self.repo.product_list = self.repo.filter_by_discount(discount)
                elif choice == '4':
                    min_price = float(input('Enter the minimum price: \n> '))
                    max_price = float(input('Enter the maximum price: \n> '))
                    self.repo.product_list = self.repo.filter_by_price_range(min_price, max_price)
                elif choice == '5':
                    min_discount = int(input('Enter the minimum discount: \n> '))
                    max_discount = int(input('Enter the maximum discount: \n> '))
                    self.repo.product_list = self.repo.filter_by_discount_range(min_discount, max_discount)
                elif choice == '0':
                    continue
                else:
                    print('Invalid choice')
            elif choice == '3':
                self.repo.product_list = self.repo.full_list
            elif choice == '4':
                self.get_scraper()
                self.repo = Repo(self.scraper.product_list)
            elif choice == '5':
                filename = input('Enter the filename (without extension): \n> ')
                self.repo.export_to_excel(filename)
            elif choice == '6':
                filename = input('Enter the filename (without extension): \n> ')
                self.repo.export_to_csv(filename)
            elif choice == '0':
                exit()
            else:
                print('Invalid choice')

    def print_product_list(self) -> None:
        print('---------------------Product List---------------------')
        for product in self.repo.product_list:
            print(product)
