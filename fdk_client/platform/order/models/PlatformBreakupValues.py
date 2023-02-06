"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class PlatformBreakupValues(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
