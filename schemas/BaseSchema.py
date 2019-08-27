from marshmallow import Schema, fields


class BaseSchema(Schema):

    id = fields.Integer(dump_only=True)
