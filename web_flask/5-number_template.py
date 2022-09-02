#!/usr/bin/python3
""" Flask module """
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ return hello message """
    return "Hello HBNB!\n"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB\n"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ return C custom message """
    text = text.replace("_", " ") 
    return f"C {text}\n"

@app.route("/python/", defaults={'text':'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ return python custom message """
    text = text.replace("_", " ")
    return f"Python {text}\n"

@app.route("/number/<n>", strict_slashes=False)
def python(n):
    """ return numbere """
    if type(n) == int:
        return n

@app.route("/number_teplate/<n>", strict_slashes=False)
def python(n):
    """ return numbere """
    if type(n) == int:
        render_template('5-number.html', n='')
        return "<body><h1>{n}<\h1><\dody>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
