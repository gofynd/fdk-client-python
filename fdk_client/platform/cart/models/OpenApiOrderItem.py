"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .MultiTenderPaymentMethod import MultiTenderPaymentMethod



from .OpenApiFiles import OpenApiFiles

























from .CartItemMeta import CartItemMeta







class OpenApiOrderItem(BaseSchema):
    #  swagger.json

    
    price_marked = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    amount_paid = fields.Float(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    cashback_applied = fields.Float(required=False)
    
    product_id = fields.Int(required=False)
    
