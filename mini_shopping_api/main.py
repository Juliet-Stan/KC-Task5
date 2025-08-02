#main.py

from typing import Dict, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cart import Cart
from product import Product

class CartItem(BaseModel):
    product_id: int
    quantity: int

app = FastAPI()
cart = Cart()

products: List[Product] = [
    Product(id=1, name='Product 1', price=10.99),
    Product(id=2, name='Product 2', price=5.99),
    Product(id=3, name='Product 3', price=7.99)
]

# The dictionary keys are integers (product IDs) and values are Product objects
products_dict: Dict[int, Product] = {product.id: product for product in products}

@app.get("/products/")
def read_products() -> List[Product]:
    """Returns a list of all available products."""
    return products

@app.post("/cart/add/")
def add_to_cart(item: CartItem) -> Dict[str, str]:
    """Adds a product to the cart with a specified quantity."""
    if item.product_id not in products_dict:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_data_to_add = products_dict[item.product_id].dict()
    product_data_to_add['quantity'] = item.quantity
    
    cart.add_product(product_data_to_add)
    cart.save_to_json()
    return {'message': 'Product added to cart'}

@app.get("/cart/checkout/")
def checkout() -> Dict[str, Any]:
    """Calculates total, returns cart content, and clears the cart."""
    # 1. Get the current cart contents
    cart_content = cart.products.copy()
    
    # 2. Calculate the total
    total: float = cart.checkout()
    
    # 3. Clear the cart
    cart.clear_cart()
    cart.save_to_json()
    
    # 4. Return the comprehensive response
    return {
        'message': 'Checkout successful!',
        'total': total,
        'cart_content': list(cart_content.values())
    }