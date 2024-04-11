#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
