import requests
from bs4 import BeautifulSoup

url = 'https://www.ksaretail.ro/shop?order=list_price+desc&search=nvme+SSD' # url of the page to scrape
response = requests.get(url) # get the page
print(response.url) # print the url of the page
soup = BeautifulSoup(response.content, 'html.parser') # parse the page using BeautifulSoup

raw_product_list = soup.find_all('div', {'class': 'o_wsale_product_grid_wrapper o_wsale_product_grid_wrapper_1_1'})
# find all the divs with class 'o_wsale_product_grid_wrapper o_wsale_product_grid_wrapper_1_1'
print(f'Total products: {len(raw_product_list)}\n') # print the number of divs (products) found
product_list = [] # list of products as tupples (name, price, link)

for product in raw_product_list: # iterate through the divs
    name = product.find('a', {'class': 'product_name'}).text.strip() # find the name of the product
    price = product.find('span', {'class': 'oe_currency_value'}).text.strip() # find the price of the product
    link = product.find('a', {'class': 'product_name'}).get('href') # find the link of the product
    link = 'https://www.ksaretail.ro' + link # add the domain url to the link

    product_list.append((name, price, link)) # add the product to the list of products for easy access

print("Products with 'wd' and '1tb' in their name:")
for product in product_list:
    name = product[0]
    price = product[1]
    if 'wd' in name.lower() and '1tb' in name.lower(): # filter the products and print the ones we care about
        print(name)
        print(f"Price: {price} RON\n")
        print(f'Link: {product[2]}')