#!/usr/bin/python3
# script that starts a Flask web application
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(err):
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
