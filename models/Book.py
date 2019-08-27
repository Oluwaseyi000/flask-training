from .BaseModel import BaseModel
from .database import db


class Book(BaseModel):

    __tablename__ = 'books'

    title = db.Column(db.String())
    description = db.Column(db.String())
    pages = db.Column(db.Integer())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
