"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ProductDetailFeature(BaseSchema):
    #  swagger.json

    
    similar = fields.List(fields.Str(required=False), required=False)
    
    seller_selection = fields.Boolean(required=False)
    
    update_product_meta = fields.Boolean(required=False)
    
    request_product = fields.Boolean(required=False)
    
