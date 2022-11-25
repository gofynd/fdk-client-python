"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Size import Size

from .ProductDetails import ProductDetails



from .ProductGroupPrice import ProductGroupPrice












class ProductInGroup(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    
    auto_select = fields.Boolean(required=False)
    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    max_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    

