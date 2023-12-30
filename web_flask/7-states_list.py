#!/usr/bin/python3
"""A python script that starts a Flask app and fetches data from database"""

#  import statements
from flask import Flask
from flask import render_template
from models import storage

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """It renders a template and dynamically embeds a variable."""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_even(n):
    """A method that checks if a url contains an even or odd number."""
    return render_template("6-number_odd_or_even.html", number=n)

@app.route("/states_list", strict_slashes=False)
def states():
    """Returns a list of all state object in database."""
    objects = storage.all()
    obj = objects.values()
    return render_template("7-states_list.html", obj=obj)


@app.teardown_appcontext
def clean_up(exc):
    """Closes resources such as db connection."""
    if exc is not None:
        print("An error occurred")
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
