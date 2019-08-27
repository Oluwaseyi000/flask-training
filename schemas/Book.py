from marshmallow import fields
from .BaseSchema import BaseSchema


class BookSchema(BaseSchema):

    title = fields.String(required=True, nullable=False)
    description = fields.String(required=True)
    pages = fields.Integer()
    author_id = fields.Integer(required=True, nullable=False)
