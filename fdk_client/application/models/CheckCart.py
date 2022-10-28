"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from .PaymentSelectionLock import PaymentSelectionLock







from .CartProductInfo import CartProductInfo



from .ShipmentPromise import ShipmentPromise



from .CartBreakup import CartBreakup

















from .CartCurrency import CartCurrency


class CheckCart(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    user_type = fields.Str(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    cod_message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    error_message = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    store_code = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    coupon_text = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    gstin = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    

