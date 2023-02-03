"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Price(BaseSchema):
    #  swagger.json

    
    currency = fields.Str(required=False)
    
    min_marked = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    
    max_marked = fields.Float(required=False)
    
    min_effective = fields.Float(required=False)
    
