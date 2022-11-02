"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .LimitedProductData import LimitedProductData









from .Price import Price



from .Size import Size







class GetProducts(BaseSchema):
    #  swagger.json

    
    allow_remove = fields.Boolean(required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    product_uid = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    price = fields.Nested(Price, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    auto_select = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    