#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


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

@babel.localeselector
def get_locale():
    """
    get local langauge
    """
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGAUGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def hello_world():
    """
    return simple greeting
    """
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
