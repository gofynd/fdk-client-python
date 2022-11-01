"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSchema import UserSchema



class UserSearchResponseSchema(BaseSchema):
    #  swagger.json

    
    users = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
