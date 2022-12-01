"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .UserSchema import UserSchema



class AuthSuccess(BaseSchema):
    #  swagger.json

    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    user = fields.Nested(UserSchema, required=False)
    
