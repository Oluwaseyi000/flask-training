import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_LOCAL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY')


# basedir = os.path.abspath(os.path.dirname(__file__))
