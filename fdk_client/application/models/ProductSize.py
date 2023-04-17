"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Dimension import Dimension



from .Weight import Weight




class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    value = fields.Str(required=False)
    

