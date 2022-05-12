from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, pwd):
        self.username = username
        self.password_hash = generate_password_hash(pwd)

    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def validate_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)
