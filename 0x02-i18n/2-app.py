#!/usr/bin/env python3

"""Module sets up a Flask application with multilingual support"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Locates the user's preferred language
    based on the `Accept-Language` header.

    Returns:
        The best-matching language or local default language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
