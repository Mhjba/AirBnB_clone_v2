#!/usr/bin/python3
""" start a flask web app  """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display “HBNB” """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ display “C ” (text) """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ display “Python ” (text) """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number(n):
    """ display “n is a number” """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """  display a HTML page """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
