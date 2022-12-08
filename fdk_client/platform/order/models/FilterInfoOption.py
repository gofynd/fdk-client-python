"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class FilterInfoOption(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
