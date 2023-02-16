"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class WeightResponse1(BaseSchema):
    #  swagger.json

    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
