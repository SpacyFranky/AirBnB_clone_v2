#!/usr/bin/python3
"""A script that starts a Flask web application:
   - web application must be listening on 0.0.0.0, port 5000
   - /: displays "Hello HBNB!"
   - /hbnb: displays "HBNB" """

from flask import Flask

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
