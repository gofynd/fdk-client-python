"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class BagBreakupValues(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
