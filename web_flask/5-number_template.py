#!/usr/bin/python3
# script that starts a Flask web application
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:s>')
def python(s="is cool"):
    get = s.replace("_", " ")
    return "Python {}".format(get)


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', Nums=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
