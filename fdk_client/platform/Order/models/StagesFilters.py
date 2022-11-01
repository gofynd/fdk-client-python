"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Options import Options



class StagesFilters(BaseSchema):
    #  swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    options = fields.Nested(Options, required=False)
    
