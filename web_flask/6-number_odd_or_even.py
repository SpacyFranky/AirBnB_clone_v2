#!/usr/bin/python3
"""A script that starts a Flask web application:
   - web application must be listening on 0.0.0.0, port 5000
   - /: displays "Hello HBNB!"
   - /hbnb: displays "HBNB" """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints 'Hello HBNB!'
    """
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints 'HBNB'
    """
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """prints "C " followed by the value of the text variable
       (replacing underscore _ symbols with a space)
    """
    text = text.replace('_', ' ')
    return("C {}".format(text))


@app.route('/python/', strict_slashes=False)
def pythoniscool():
    """prints "Python is cool"
    """
    return("Python is cool")


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """prints "Python ", followed by the value of the text variable
       (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints "n is a number" only if n in an integer
    """
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a HTML page only if n is an integer
       H1 tag: Number: n inside the tag BODY
    """
    return(render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """displays a HTML page only if n is an integer
       H1 tag: Number: n is even|odd inside the tag BODY
    """
    if n % 2 == 0:
        return(render_template('6-number_odd_or_even.html', n=n,
                               evorod="even"))
    else:
        return(render_template('6-number_odd_or_even.html', n=n,
                               evorod="odd"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
