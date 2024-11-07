#!/usr/bin/env python3

"""Module sets up a Flask application with multilingual support"""

from flask import Flask, render_template, request
from flask_babel import Babel
import pytz

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the login parameter from the function url
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit() and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Sets the current user on `flask.g` based on the `login_as` parameter.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Locates the user's preferred language header.

    Returns:
        The best-matching language or local default language.
    """
    if 'locale' in request.args and request.args['locale'] in app.config[
            'LANGUAGES']:
        return request.args['locale']
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    local = request.accept_languages.best_match(app.config['LANGUAGES'])
    if local:
        return local
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Attempts to get the user's preferred timezone from various sources.

    Returns:
        The user's timezone or the default timezone.
    """
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return pytz.timezone(user_timezone).zone
            except pytz.UnknownTimeZoneError:
                pass

    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
