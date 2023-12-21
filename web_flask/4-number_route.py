#!/usr/bin/python3
"""A python script that starts a Flask app and handles dynamic routes"""

from flask import Flask

app = Flask(__name__)

# making routes


@app.route("/", strict_slashes=False)
def root():
    """Handles request for the root."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles request for hbnb."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def dynamic(text):
    """Handles a route with a dynamic parameter."""
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def dynamic_two(text="is cool"):
    """Another function that handles a dynamic route parameter."""
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_integer(n):
    """It checks if a dynamic route parameter is an integer."""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
