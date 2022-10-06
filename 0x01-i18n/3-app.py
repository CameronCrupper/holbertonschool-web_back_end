#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel, _
from flask import request


class Config():
    """
    configure babel
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
    gets the loacl language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    basic greeting
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
