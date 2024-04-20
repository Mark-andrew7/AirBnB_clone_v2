#!/usr/bin/python3
"""
Starts a web flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """
    Displays hello bnb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Display c
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_p(text):
    """
    Display python
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """
    Display n is a number
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """
    Display html page
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_html1(n):
    """
    Display html page
    """
    return render_template("6-number_odd_or_even.html", "number"=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
