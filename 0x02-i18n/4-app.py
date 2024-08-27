#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Return the index page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
