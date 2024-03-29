#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel, _
from flask import request, g
from typing import Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """
    configure babel
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
    before request
    """
    user: dict = get_user()
    print(user)
    g.user = user

def get_user() -> Union[dict, None]:
    """
    get user
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
    gets the loacl language
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """
    basic greeting
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
