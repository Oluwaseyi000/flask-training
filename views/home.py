from flask_restplus import Resource
from flask import request, make_response
import jwt
import datetime
import os

from ..models.User import UserModel
from ..schemas.User import UserSchema
from ..schemas.Book import BookSchema
# from ..utils.decorated import validate_use
from ..utils.authenticate import token_required
from ..utils.authenticate import assignToken

from ..run import api
from ..models.database import db

@api.route('/user')
class UserResource(Resource):

    @token_required
    def get(self):
      
        users = UserModel.query.all()
        result = UserSchema(many=True).dump(users).data
      
        return {'result': result,
                'token': request.token}

    def post(self):
        data = request.get_json()
        user = UserSchema().load(data)
        if user.errors:
            return dict(errors=user.errors, message='An error occurred')

        userbody = UserModel(**user.data)
        db.session.add(userbody)
        db.session.commit()
        token = assignToken(user.data['name'], user.data['password'] )
        return {'user': user.data, 'token': token}


@api.route('/user/<user_id>')
class UserSingleResource(Resource):
    def get(self, user_id):

        if user_id == 'count':
            count = UserModel.query.count()
            return {'totalUsers': count}

        elif user_id == 'adult':
            adult = UserModel.query.filter(UserModel.age > 100).all()
            result = UserSchema(many=True).dump(adult).data
            return result

        user = UserModel.query.get_or_404(user_id)
        result = UserSchema().dump(user)
        token = assignToken(result.data['fullname'], result.data['password'])
        
        return {'user':result.data, 'token':token}

    def patch(self, user_id):
        request_data = request.get_json()
        user = UserModel.query.filter_by(id=user_id).first_or_404()
        data = UserSchema().load(request_data).data

        for attr, value in data.items():
            setattr(user, attr, value)

        db.session.commit()
        return data

    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first_or_404()
        db.session.delete(user)
        db.session.commit()
        return "deletion successful"


@api.route('/user/<author_id>/book')
class UserAuthorResource(Resource):
    def get(self, author_id):
        """ get books authored by  a user """
        author = UserModel.query.filter_by(id=author_id).first_or_404()
        user = UserSchema().dump(author).data
        books = BookSchema(many=True).dump(author.books).data
        return {'authors': author.name, 'books': books}
        # return books


@api.route('/auth/login')
class AuthResource(Resource):
    def get(self):
        auth = request.authorization
        print(auth)

        if auth and auth.password == 'a1b2c3d4e5':
            token = jwt.encode({
                'user': {'name': auth.username, 'password': auth.password},
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                os.getenv('SECRET_KEY')
            )
            return {'token': token.decode('UTF-8')}

        return make_response('could not verify', 401, {'www-authenticate': 'Basic loing reqire'})
        # return 'could not veryfi'
