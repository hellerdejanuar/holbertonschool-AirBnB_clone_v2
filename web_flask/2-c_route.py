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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
