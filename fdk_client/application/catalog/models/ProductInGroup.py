"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductGroupPrice import ProductGroupPrice









from .ProductDetails import ProductDetails



from .Size import Size







class ProductInGroup(BaseSchema):
    #  swagger.json

    
    auto_select = fields.Boolean(required=False)
    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    product_uid = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
