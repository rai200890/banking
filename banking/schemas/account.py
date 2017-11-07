from marshmallow import Schema, fields, ValidationError


def validate_balance(value):
    if value <= 0:
        raise ValidationError("Initial balance must be greater than 0")


class AccountSchema(Schema):
    client_id = fields.Int(required=True)
    agency_id = fields.Int(required=True)
    password = fields.Str(required=True)
    initial_balance = fields.Decimal(required=True, validation=validate_balance)
