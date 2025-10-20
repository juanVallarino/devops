from marshmallow import Schema, fields, validate

class BlacklistSchema(Schema):
    email = fields.Str(required=True, validate=validate.Email())
    app_uuid = fields.Str(required=True, validate=validate.Length(min=1))
    blocked_reason = fields.Str(required=True, validate=validate.Length(min=1))

class BlacklistResponseSchema(Schema):
    email = fields.Str()
    app_uuid = fields.Str()
    blocked_reason = fields.Str()
    is_blocked = fields.Bool()
    message = fields.Str()
