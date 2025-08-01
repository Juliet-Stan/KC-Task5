# Mini Shopping API with Cart

A FastAPI-based API to manage products and shopping cart.

## Features
* Create, read, and manage products
* Add products to cart
* View cart contents
* Checkout cart
* Store data in a JSON file
* Use try-except blocks for error handling
* Version control using Git

## Endpoints
* `POST /products/`: Create a new product
* `GET /products/`: Get all products
* `POST /cart/add/`: Add a product to cart
* `GET /cart/`: Get cart contents
* `POST /cart/checkout/`: Checkout cart

## Usage
1. Clone the repository: `git clone https://github.com/your-username/mini-shopping-api.git`
2. Navigate to the project directory: `cd mini-shopping-api`
3. Install dependencies: `pip install fastapi uvicorn`
4. Run the application: `uvicorn main:app --reload`
5. Use a tool like curl or Postman to test the API

## Example Requests
* Create a new product: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Product 1", "price": 10.99}' http://localhost:8000/products/`
* Add a product to cart: `curl -X POST -H "Content-Type: application/json" -d '{"product_id": 1, "quantity": 2}' http://localhost:8000/cart/add/`
* Get cart contents: `curl -X GET http://localhost:8000/cart/`
* Checkout cart: `curl -X POST http://localhost:8000/cart/checkout/`


