#!/usr/bin/python3
# script that starts a Flask web application
from models import *
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


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', Nums=n)


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.route('/cities_by_states')
def cities_by_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
