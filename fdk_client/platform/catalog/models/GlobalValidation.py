"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Properties import Properties







class GlobalValidation(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    definitions = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    properties = fields.Nested(Properties, required=False)
    
    type = fields.Str(required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    