"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ProductBundleItem(BaseSchema):
    #  swagger.json

    
    max_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    product_uid = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
