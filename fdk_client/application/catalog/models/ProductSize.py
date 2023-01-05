"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .Weight import Weight





from .Dimension import Dimension





class ProductSize(BaseSchema):
    #  swagger.json

    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    quantity = fields.Int(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    value = fields.Str(required=False)
    
