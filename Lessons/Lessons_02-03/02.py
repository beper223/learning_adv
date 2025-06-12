# Написать маршрут, который удаляет элемент из списка data.
data = ["apple", "banana", "cherry"]

from flask import Flask

app = Flask(__name__)

@app.route('/fruits/<string:name>', methods=['DELETE'])
def hello_world(name):  # put application's code here
    if name in data:
        data.remove(name)
        return {"message": "Item successfully deleted"}, 204
    else:
        return {"message": "Item not found"}, 404