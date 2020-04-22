#!/usr/bin/python3
# script that starts a Flask web application
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<string:s>')
def c(s):
    get = s.replace("_", " ")
    return "C {}".format(get)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
