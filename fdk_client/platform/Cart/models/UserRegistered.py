"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UserRegistered(BaseSchema):
    #  swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
