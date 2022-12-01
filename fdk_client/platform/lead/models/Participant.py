"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSchema import UserSchema







class Participant(BaseSchema):
    #  swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    identity = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
