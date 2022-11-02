"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSchema import UserSchema



class UserObjectSchema(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    