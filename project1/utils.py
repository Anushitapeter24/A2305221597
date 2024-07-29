import requests
import uuid

API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIyMjQxMzg2LCJpYXQiOjE3MjIyNDEwODYsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImI2ODE0NWU5LWU0ZmYtNGQ4Zi04ZjAxLWM2NTg1MmYzYjI4ZiIsInN1YiI6ImFudXNoaXRhcGV0ZXIyNDZAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiQU1JVFkgVU5WRVJTSVRZIE5PSURBIiwiY2xpZW50SUQiOiJiNjgxNDVlOS1lNGZmLTRkOGYtOGYwMS1jNjU4NTJmM2IyOGYiLCJjbGllbnRTZWNyZXQiOiJ3UHdUckN4cG5DZkxaSVp6Iiwib3duZXJOYW1lIjoiQU5VU0hJVEEgUEVURVIiLCJvd25lckVtYWlsIjoiYW51c2hpdGFwZXRlcjI0NkBnbWFpbC5jb20iLCJyb2xsTm8iOiJBMjMwNTIyMTU5NyJ9.9TUTSDsOx-CUNRAlVrH59meZhA7Hy_rruPArqu9dO7M"

def fetch_products(categoryname, n, page, sort_by, sort_order, min_price, max_price):
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    products = []
    ECOMMERCE_API_ENDPOINTS = [
        "http://api1.example.com",
        "http://api2.example.com",
        "http://api3.example.com",
        "http://api4.example.com",
        "http://api5.example.com"
    ]
    for endpoint in ECOMMERCE_API_ENDPOINTS:
        response = requests.get(f"{endpoint}/categories/{categoryname}/products", headers=headers)
        if response.status_code == 200:
            products.extend(response.json())

    filtered_products = [
        product for product in products 
        if min_price <= product['price'] <= max_price
    ]

    sorted_products = sorted(filtered_products, key=lambda x: x[sort_by], reverse=(sort_order == 'desc'))

    start = (page - 1) * n
    end = start + n
    paginated_products = sorted_products[start:end]

    for product in paginated_products:
        product['unique_id'] = str(uuid.uuid4())

    return paginated_products

def fetch_product_details(categoryname, productid):
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    ECOMMERCE_API_ENDPOINTS = [
        "http://api1.example.com",
        "http://api2.example.com",
        "http://api3.example.com",
        "http://api4.example.com",
        "http://api5.example.com"
    ]
    for endpoint in ECOMMERCE_API_ENDPOINTS:
        response = requests.get(f"{endpoint}/categories/{categoryname}/products/{productid}", headers=headers)
        if response.status_code == 200:
            product = response.json()
            product['unique_id'] = productid
            return product
    return {}
