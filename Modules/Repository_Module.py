from pandas import DataFrame

class Repo:
    # This class is responsible for storing the products and the operations that can be performed on them
    def __init__(self, product_list: list):
        self.product_list = product_list
        self.full_list = product_list
    
    # The sort functions actually modify the list, so they don't return anything
    def sort_by_name(self) -> None:
        self.product_list.sort(key=lambda product: product.name)
    
    def sort_by_price(self) -> None:
        self.product_list.sort(key=lambda product: product.curr_price)
    
    def sort_by_discount(self) -> None:
        self.product_list.sort(key=lambda product: product.discount, reverse=True)
    
    def get_product_list(self) -> list:
        # return the product list
        return self.product_list
    
    # The filter functions return a list with the products that match the given criteria without modifying the original list
    def filter_by_name(self, name: str) -> list:
        # return a list with the products that contain the name in their name
        return [product for product in self.product_list if name in product.name]

    def filter_by_price(self, price: float) -> list:
        # return a list with the products that cost the given price
        return [product for product in self.product_list if price == product.curr_price]
    
    def filter_by_discount(self, discount: int) -> list:
        # return a list with the products that have the given discount
        return [product for product in self.product_list if discount == product.discount]
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> list:
        # return a list with the products that cost between the given prices
        return [product for product in self.product_list if min_price <= product.curr_price <= max_price]
    
    def filter_by_discount_range(self, min_discount: int, max_discount: int) -> list:
        # return a list with the products that have a discount between the given discounts
        return [product for product in self.product_list if min_discount <= product.discount <= max_discount]
    
    def export_to_excel(self):
        # export the product list to an excel file
        df = DataFrame([product.to_dict() for product in self.product_list])
        df.to_excel('products.xlsx')
