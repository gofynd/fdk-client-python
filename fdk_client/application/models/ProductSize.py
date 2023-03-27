"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Dimension import Dimension







from .Weight import Weight






class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    dimension = fields.Nested(Dimension, required=False)
    
    display = fields.Str(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    is_available = fields.Boolean(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    

