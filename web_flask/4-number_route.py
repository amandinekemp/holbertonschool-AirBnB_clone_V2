#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask


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
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display a message"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display a message"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
