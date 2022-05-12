import os

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///'+os.path.join(os.getcwd(), 'dev.db'))
print(SQLALCHEMY_DATABASE_URI)
