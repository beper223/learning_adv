# Написать маршрут, который будет принимать роль и действие и возвращать
# True/False по permissions.

from flask import Flask

app = Flask(__name__)

permissions = {
"admin": ["create", "delete", "update"],
"editor": ["update"],
"user": ["read"]
}

@app.route('/protected/<string:role>/<string:perm>')
def get_perm(role,perm):  # put application's code here
    # http://127.0.0.1:5000/protected/admin/delete
    a = permissions.get(role,[])
    return {"allowed": perm in a}
    # if perm in a:
    #     return 'User found' #"Gut", 204
    # else:
    #     return 'User not found' #"Nicht gut", 205
    # if a and perm in a:
    #     return {"message": "Gut"}, 204
    # else:
    #     return {"message": "Nicht gut"}, 205