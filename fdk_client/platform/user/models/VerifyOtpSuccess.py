"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSchema import UserSchema







class VerifyOtpSuccess(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    user_exists = fields.Boolean(required=False)
    
    register_token = fields.Str(required=False)
    
