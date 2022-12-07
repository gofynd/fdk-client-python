"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CartBreakup import CartBreakup













from .CartProductInfo import CartProductInfo



from .ShipmentPromise import ShipmentPromise











from .CartCurrency import CartCurrency



from .PaymentSelectionLock import PaymentSelectionLock



class CartDetailResponse(BaseSchema):
    #  swagger.json

    
    coupon_text = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    