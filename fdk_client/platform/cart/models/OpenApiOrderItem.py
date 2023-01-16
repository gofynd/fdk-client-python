"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .CartItemMeta import CartItemMeta









from .MultiTenderPaymentMethod import MultiTenderPaymentMethod



from .OpenApiFiles import OpenApiFiles

















class OpenApiOrderItem(BaseSchema):
    #  swagger.json

    
    employee_discount = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    price_marked = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    product_id = fields.Int(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    cod_charges = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
