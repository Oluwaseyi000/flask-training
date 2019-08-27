from .BaseModel import BaseModel
from .database import db


class UserModel(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'the user name is {}'.format(self.name)
