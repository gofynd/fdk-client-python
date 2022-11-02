"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class WeightResponse(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
