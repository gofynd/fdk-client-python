"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .StagesFilters import StagesFilters



class Stages(BaseSchema):
    #  swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    
