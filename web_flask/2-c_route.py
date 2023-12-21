#!/usr/bin/python3
"""A python script that starts a Flask application and handles dynaic routes"""

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
