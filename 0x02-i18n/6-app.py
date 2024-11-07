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

users = {
    1: {"name": "Balou", "locale": "fr", "locale": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user ID from the request URL's `login_as` parameter.

    Returns:
        The user dictionary if found, otherwise None.
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
    Locates the user's preferred language based on the following order:

    1. query parameter.
    2. user information (when logged in).
    3. Best-matching language.
    4. Local Defualtconfiguration.
    Returns:
        The locale proritorizing user preferred local.
    """
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    if 'locale' in request.args and request.args['locale'] in app.config[
            'LANGUAGES']:
        return request.args['locale']

    local = request.accept_languages.best_match(app.config['LANGUAGES'])
    if local:
        return local
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
