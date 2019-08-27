from marshmallow import fields, validates, post_load, ValidationError
from .BaseSchema import BaseSchema
from ..models.User import UserModel


def validate_age(age):
    print('the age got here')
    if age < 25:
        raise ValidationError('oldethat is too young')


class UserSchema(BaseSchema):
    name = fields.String(required=True, dump_to="fullname")
    age = fields.Integer()
    password = fields.String()

    # @post_load()
    # def post(self, data):
    #     return UserModel(**data)

    @validates('age')
    def validate_age(self, age=12):
        if age < 25:
            raise ValidationError('that is too young')
