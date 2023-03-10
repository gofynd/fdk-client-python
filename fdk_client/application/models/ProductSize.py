"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Weight import Weight









from .Dimension import Dimension




class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    weight = fields.Nested(Weight, required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    quantity = fields.Int(required=False)
    

