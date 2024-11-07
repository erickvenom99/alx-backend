#!/usr/bin/env python3

"""Module sets up a Flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns:
        renders the index.html page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
