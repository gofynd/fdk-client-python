"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSchema import UserSchema



class CreateUserResponseSchema(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
