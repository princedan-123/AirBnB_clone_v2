#!/usr/bin/python3
"""A python script that starts a Flask application."""

from flask import Flask

app = Flask(__name__)

# making a route


@app.route("/")
def root():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
