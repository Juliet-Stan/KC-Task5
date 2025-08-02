import json
import math
from product import Product

class Cart:
    def _init_(self):
        self.products = {}

    def add_product(self, product_id: int, quantity: int):
        
        if product_id in self.products:
            self.products[product_id]['quantity'] += quantity
        else:
           
            self.products[product_id] = {
                'id': product_id,
                'name': f"Product {product_id}",
                'price': 0.0,
                'quantity': quantity
            }
        
    def checkout(self):
        total = 0
        for product in self.products.values():
            total += product['quantity'] * product['price']
        return math.round(total, 2)

    def save_to_json(self):
        with open('cart.json', 'w') as f:
            json.dump(self.products, f)

    def load_from_json(self):
        try:
            with open('cart.json', 'r') as f:
                self.products = json.load(f)
        except FileNotFoundError:
            pass