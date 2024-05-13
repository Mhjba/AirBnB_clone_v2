#!/usr/bin/python3
""" start a flask web app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """ display "Hello HBNB!" """
    return render_template("10-hbnb_filters.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
