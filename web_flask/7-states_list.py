#!/usr/bin/python3
"""Start flask app for HBNB """
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays an HTML page """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(app):
    """ declare a method to handle """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
