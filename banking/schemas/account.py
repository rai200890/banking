from marshmallow import Schema, fields


class AccountSchema(Schema):
    password = fields.Str()
    client_id = fields.Int()
    agency_id = fields.Int()
