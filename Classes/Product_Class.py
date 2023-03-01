from math import ceil


class Product:
    def __init__(self, name=None, curr_price=None, full_price=None, link=None) -> None:
        self.name = name
        self.curr_price = curr_price
        self.full_price = full_price
        self.link = link
        self.discount = self.get_discount()
    
    def get_discount(self) -> float:
        if self.full_price is None:
            return 0
        else:
            return ceil((1 - (self.curr_price / self.full_price)) * 100)
        
    def __str__(self) -> str:
        return f'\nProduct: {self.name}\nPrice: {self.curr_price} (of site currency) - Discount: {self.discount}% \nLink: {self.link}'
    
    def to_dict(self) -> dict:
        return {
            'Product Name': self.name,
            'Current Price': self.curr_price,
            'Full Price': self.full_price,
            'Discount': self.discount,
            'Link': self.link,
        }