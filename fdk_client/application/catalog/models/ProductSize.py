"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Dimension import Dimension







from .Weight import Weight









class ProductSize(BaseSchema):
    #  swagger.json

    
    dimension = fields.Nested(Dimension, required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
