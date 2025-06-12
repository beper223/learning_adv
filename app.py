# Фильтрация списка по query params
# ТЗ: GET /products # В products лежит список словарей.
# Поддерживаются query-параметры: min_price, max_price, category.
# Нужно реализовать получение записей по фильтрам через query params
# http://127.0.0.1:5000/products — вернёт весь список
# http://127.0.0.1:5000/products?min_price=50 — только товары с ценой ≥ 50
# http://127.0.0.1:5000/products?max_price=500&category=electronics — только электронику до 500

from flask import Flask, request, jsonify

app = Flask(__name__)
products = [
    {"id": 1, "name": "Chair", "price": 45, "category": "furniture"},
    {"id": 2, "name": "Sofa", "price": 120, "category": "furniture"},
    {"id": 3, "name": "Laptop", "price": 1000, "category": "electronics"}
]

@app.route('/products', methods=['GET'])
def get_products():
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    category = request.args.get('category', type=str)

    filtered = products
    if min_price is not None:
        filtered = [p for p in filtered if p['price'] >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p['price'] <= max_price]
    if category:
        filtered = [p for p in filtered if p['category'] == category]

    return jsonify(filtered)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
