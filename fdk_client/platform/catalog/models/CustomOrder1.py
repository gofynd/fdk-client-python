"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CustomOrder1(BaseSchema):
    #  swagger.json

    
    manufacturing_time_unit = fields.Str(required=False)
    
    is_custom_order = fields.Boolean(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
