"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .MultiTenderPaymentMethod import MultiTenderPaymentMethod





from .ShippingAddress import ShippingAddress

















from .OpenApiOrderItem import OpenApiOrderItem





from .OpenApiFiles import OpenApiFiles





from .ShippingAddress import ShippingAddress





class OpenApiPlatformCheckoutReq(BaseSchema):
    #  swagger.json

    
    cod_charges = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    coupon_code = fields.Str(required=False)
    
    employee_discount = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    coupon = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    order_id = fields.Str(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    cashback_applied = fields.Float(required=False)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    currency_code = fields.Str(required=False)
    
