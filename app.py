from flask import Flask, render_template, jsonify
import database as db

app = Flask(__name__)


@app.route('/')
def route_home():
    return 'Olá Mundo!'


if __name__ == '__main__':
    app.run(debug=True)
