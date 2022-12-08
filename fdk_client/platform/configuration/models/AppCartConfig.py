"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DeliveryCharges import DeliveryCharges















class AppCartConfig(BaseSchema):
    #  swagger.json

    
    delivery_charges = fields.Nested(DeliveryCharges, required=False)
    
    enabled = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    min_cart_value = fields.Float(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
    empty_cart = fields.Boolean(required=False)
    
