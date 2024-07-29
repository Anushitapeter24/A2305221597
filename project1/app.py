from flask import Flask, request, jsonify
from utils import fetch_products, fetch_product_details

app = Flask(__name__)

@app.route('/categories/<categoryname>/products', methods=['GET'])
def get_top_products(categoryname):
    n = int(request.args.get('n', 10))
    page = int(request.args.get('page', 1))
    sort_by = request.args.get('sort_by', 'rating')
    sort_order = request.args.get('sort_order', 'desc')
    min_price = float(request.args.get('min_price', 0))
    max_price = float(request.args.get('max_price', float('inf')))

    products = fetch_products(categoryname, n, page, sort_by, sort_order, min_price, max_price)
    return jsonify(products)
@app.route('/')
def index():
    n = request.args.get('n')
    page = request.args.get('page')
    sort_by = request.args.get('sort_by')
    sort_order = request.args.get('sort_order')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    # Process these parameters and return the appropriate response
    return f'n={n}, page={page}, sort_by={sort_by}, sort_order={sort_order}, min_price={min_price}, max_price={max_price}'


@app.route('/categories/<categoryname>/products/<productid>', methods=['GET'])
def get_product_details(categoryname, productid):
    product_details = fetch_product_details(categoryname, productid)
    return jsonify(product_details)

if __name__ == '__main__':
    app.run(debug=True)
