from marshmallow import fields, validate, exceptions as marsh_exceptions
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=validate.Length(1, 50))
    last_name = fields.String(required=True, validate=validate.Length(1, 50))
    username = fields.String(required=True, validate=validate.Length(1, 50))
    password = fields.String(load_only=True, validate=validate.Length(1))
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @classmethod
    def validate_password(cls, password):
        if len(password) < 8:
            raise marsh_exceptions.ValidationError(
                message={"password": "Invalid password format"}
            )
