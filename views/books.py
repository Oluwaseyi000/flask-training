from flask_restplus import Resource
from flask import request

from ..schemas.Book import BookSchema
from ..schemas.User import UserSchema
from ..models.Book import Book
from ..models.database import db

from ..run import api


@api.route('/book')
class BookResource(Resource):
    def post(self):
        request_data = request.get_json()
        book_schema = BookSchema().load(request_data)

        if book_schema.errors:
            return dict(errors=book_schema.errors, message='An error occured')

        new_book = Book(**book_schema.data)

        db.session.add(new_book)
        db.session.commit()

        return book_schema

    def get(self):
        query = Book.query.all()
        books = BookSchema(many=True).dump(query).data

        return books


@api.route('/book/<param>')
class BookSingleResource(Resource):
    def get(self, param):
        """ get  a  single book """

        book = Book.query.get_or_404(param)
        result = BookSchema().dump(book)
        return result.data

    def patch(self, param):
        """ edit  a book """
        request_data = request.get_json()
        book = Book.query.get_or_404(param)
        data = BookSchema().load(request_data).data

        for attr, value in data.items():
            setattr(book, attr, value)

        db.session.commit()
        return BookSchema().dump(book)

    def delete(self, param):
        """ delete a book """
        book = Book.query.get_or_404(param)
        db.session.delete(book)
        db.session.commit()
        return "book successfully deleted "


@api.route('/book/<book_id>/author')
class BookAuthorResource(Resource):
    def get(self, book_id):
        author = Book.query.filter_by(id=book_id).first_or_404().author
        return UserSchema().dump(author)
