#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
	"""Display a message"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
	"""Display a message"""
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
	"""Display a message"""
	text = text.replace('_', ' ')
	return f"C {text}"

if __name__ == '__main__':
	app.run(port=5000, host='0.0.0.0')
