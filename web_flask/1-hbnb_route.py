#!/usr/bin/python3
"""A python script that starts a Flask application."""

from flask import Flask

app = Flask(__name__)

# making a route


@app.route("/", strict_slashes=False)
def root():
    """Handles request for the root."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles request for hbnb."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
