#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"

if __name__ == '__main__':
	app.run(port=5000, host='0.0.0.0')
