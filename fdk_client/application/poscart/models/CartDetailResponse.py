"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CartCurrency import CartCurrency

















from .ShipmentPromise import ShipmentPromise





from .PaymentSelectionLock import PaymentSelectionLock



from .CartProductInfo import CartProductInfo





from .CartBreakup import CartBreakup



class CartDetailResponse(BaseSchema):
    #  swagger.json

    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    comment = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    