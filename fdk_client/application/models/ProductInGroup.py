"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductGroupPrice import ProductGroupPrice



from .ProductDetails import ProductDetails

from .Size import Size












class ProductInGroup(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    auto_select = fields.Boolean(required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    

