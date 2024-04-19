#!/usr/bin/python3
"""Start flask app for HBNB """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(app):
    """Declare a method to handle """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
