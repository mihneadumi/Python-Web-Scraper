import os
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
        os.system('cls')
        self.scraper = None
        while self.scraper is None:
            link = input('Enter the link to the page with the products or "exit" to close: \n> ')
            if 'ksaretail' in link:
                self.scraper = KSA_Scraper(link)
            elif 'altex.ro' in link:
                self.scraper = Altex_Scraper(link)
            elif link == 'exit':
                exit()
            else:
                os.system('cls')
                print('No scraper for this site yet')

    def start_app(self):
        while True:
            # os.system('cls')
            self.print_product_list()
            print('\n---------------------Menu---------------------\n')
            print('Currently scraping: ' + self.scraper.name)
            print('1. Sort the product list')
            print('2. Filter the product list')
            print('3. Remove filters')
            print('4. Scrape a different link')
            print('5. Exit')
            choice = input('> ')
            if choice == '1':
                os.system('cls')
                print('---------------------Sort Menu---------------------')
                print('1. Sort by name')
                print('2. Sort by price')
                print('3. Sort by discount')
                print('4. Back')
                choice = input('> ')
                if choice == '1':
                    self.repo.sort_by_name()
                elif choice == '2':
                    self.repo.sort_by_price()
                elif choice == '3':
                    self.repo.sort_by_discount()
                elif choice == '4':
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
                print('6. Back')
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
                elif choice == '6':
                    continue
                else:
                    print('Invalid choice')
            elif choice == '3':
                self.repo.product_list = self.repo.full_list
            elif choice == '4':
                self.get_scraper()
                self.repo = Repo(self.scraper.product_list)
            elif choice == '5':
                exit()
            else:
                print('Invalid choice')

    def print_product_list(self) -> None:
        print('---------------------Product List---------------------')
        for product in self.repo.product_list:
            print(product)
