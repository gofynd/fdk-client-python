"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class FilterInfoOption(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
