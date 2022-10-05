#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask
from flask import render_template
from flask import request, g
from flask_babel import Babel, _
from typing import Union
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """
    Configuration for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)

@app.before_request
def before_request(login_as: int = None):
    """
    request each function
    """
    user: dict = get_user()
    g.user = user

def get_user() -> Union[dict, None]:
    """
    get dictionary user
    """
    login_user = request.args.get('login_as', None)
    if login_user is None:
        return None
    user: dict = {}
    user[login_user] = users.get(int(login_user))
    return user[login_user]

@babel.localeselector
def get_locale():
    """
    get local langauge
    """
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGAUGES']:
        return locale

    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    """
    finds timezone
    """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tzone = pytz.timezone(timezone)
        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tzone = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tzone = pytz.timezone(timezone)

    except exceptions.UnknownTimeZoneError:
        timezone = 'UTC'

    return timezone

@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """
    return simple greeting
    """
    return render_template('7-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
