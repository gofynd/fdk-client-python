"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class JsonSchema(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    tooltip = fields.Str(required=False)
    
