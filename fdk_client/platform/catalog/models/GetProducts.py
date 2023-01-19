"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Size import Size











from .Price import Price





from .LimitedProductData import LimitedProductData



class GetProducts(BaseSchema):
    #  swagger.json

    
    auto_select = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    min_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    
    price = fields.Nested(Price, required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
