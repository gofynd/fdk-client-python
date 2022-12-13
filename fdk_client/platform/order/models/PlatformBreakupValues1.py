"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class PlatformBreakupValues1(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
