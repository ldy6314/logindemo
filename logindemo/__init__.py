from flask import Flask
from .blueprint import bp
from .extensions import db


def create_app():
    app = Flask('logindemo')
    app.register_blueprint(bp)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    return app
