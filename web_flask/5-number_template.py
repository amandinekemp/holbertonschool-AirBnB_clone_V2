#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Display a message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """Display a message"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display a message"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display a message"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:num>", strict_slashes=False)
def number_template(num):
    """Display a message"""
    return render_template('5-number.html', n=num)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
