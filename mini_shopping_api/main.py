from fastapi import FastAPI, HTTPException
from product import Product
from cart import Cart

app = FastAPI()

cart = Cart()
cart.load_from_json()

products = [
    Product(id=1, name='Product 1', price=10.99),
    Product(id=2, name='Product 2', price=5.99),
    Product(id=3, name='Product 3', price=7.99)
]

@app.get("/products/")
def read_products():
    return products

@app.post("/cart/add/")
def add_to_cart(product_id: int, quantity: int):
    for product in products:
        if product.id == product_id:
            cart.add_product(product_id, quantity)
            cart.save_to_json()
            return {'message': 'Product added to cart'}
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/cart/checkout/")
def checkout():
    total = cart.checkout()
    return {'total': total}
