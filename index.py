from flask import Flask, render_template, jsonify, request
from database.database import Database
app = Flask(__name__)


@app.rout('/')
def welcome():
    return 'Welcome to Hardware builder API home endpoint'


@app.route('/users', methods=['GET'])
def get_all_users():
    database = Database('users')
    res = database.get_all('users')
    return res


@app.route('/user', methods=['GET'])
def get_user():
    database = Database('users')
    username = request.args.get('username')
    user = {'username': username}
    print(database)
    res = database.get_user(user)
    return res


@app.route('/user', methods=['POST'])
def create_user():
    database = Database('users')
    username = request.args.get('username')
    password = request.args.get('password')
    res = database.create_user({'username': username, 'password': password})
    return res


if __name__ == '__main__':
    app.run(debug=True)
