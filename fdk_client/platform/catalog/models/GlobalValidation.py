"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .Properties import Properties



class GlobalValidation(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    definitions = fields.Dict(required=False)
    
    properties = fields.Nested(Properties, required=False)
    