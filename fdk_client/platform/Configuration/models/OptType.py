"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OptType(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
