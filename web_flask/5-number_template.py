#!/usr/bin/python3
""" Flask module """
from flask import Flask
from flask import render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ return number template """
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
