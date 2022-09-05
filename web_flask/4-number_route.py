#!/usr/bin/python3
""" Flask module """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ return hello message """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ return C custom message """
    text = "C " + text.replace("_", " ") 
    return text


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ return python custom message """
    text = "Python " + text.replace("_", " ")
    return text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ return number """
    if type(n) is int:
        return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
