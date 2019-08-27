

from flask import Flask, request, jsonify
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from functools import wraps


from .blueprint import api_blueprint
from .models.database import db
# from .schemas import ma


api = Api(api_blueprint)


def myDecorator(func):
    print('inside of the decorator before  caling the function')
    # func()
    # print('inside of the decorator after  caling the function')
    return func
    # return wraps


def create_app(config='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config)

    db.init_app(app)

    # ma.init_app(app)

    app.register_blueprint(api_blueprint)

    # from .models.User import UserModel
    # from .models.Book import Book

    from .models import Book, User

    # import .models

    from .views import UserResource, UserSingleResource, UserAuthorResource, BookResource, BookAuthorResource, AuthResource

    Migrate(app, db)

    def validate_user(func):

        @wraps(func)
        def decorated_function(*args, **kwargs):
            token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7Im5hbWUiOiJzZXlpIiwicGFzc3dvcmQiOiJhMWIyYzNkNGU1In0sImV4cCI6MTU2NTY5ODQ4Nn0.aP3QZgtBwWP8xrvsciUBUqSDPtII_tki2AX5O4QQ97U'
            # return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7Im5hbWUiOiJzZXlpIiwicGFzc3dvcmQiOiJhMWIyYzNkNGU1In0sImV4cCI6MTU2NTY5ODQ4Nn0.aP3QZgtBwWP8xrvsciUBUqSDPtII_tki2AX5O4QQ97U'
            setattr(request, 'decoded_token', token)
            return func(*args, **kwargs)

        return decorated_function

    # @myDecorator
    def uppercase_decorator(function):

        def wrapper():
            print('header')

            function()

            print('footer')
            # return function()
            # make_uppercase = func.upper()
            return make_uppercase

        return wrapper

    @app.route('/decorator')
    @validate_user
    def say_hi():
        print('main body')
        # print(dict(request['decoded_token']))
        # return {'token': "request['decoded_token']"}

    # @app.route('/decorator')
    # def tesdts():
    #     return print_message("Some random message")

    return app
