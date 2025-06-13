# Есть небольшой набор данных. Написать маршрут, который
# возвращает имя по user_id из этого набора данных и
# User not found -- если ничего не найдено.
#
# users = {1: "Alice", 2: "Bob", 3: "Charlie"}

from flask import Flask

app = Flask(__name__)
users = {1: "Alice", 2: "Bob", 3: "Charlie"}

@app.route('/user/<int:user_id>')
def hello_world(user_id):  # put application's code here
    name = users.get(user_id)
    if name:
        return name
    return 'User not found'