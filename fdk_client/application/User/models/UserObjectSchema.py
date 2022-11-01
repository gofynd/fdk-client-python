"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UserSchema import UserSchema



class UserObjectSchema(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
