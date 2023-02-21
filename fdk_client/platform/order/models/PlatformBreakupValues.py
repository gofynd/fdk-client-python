"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class PlatformBreakupValues(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
