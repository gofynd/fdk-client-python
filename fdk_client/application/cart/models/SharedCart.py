"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .PaymentSelectionLock import PaymentSelectionLock



from .CartProductInfo import CartProductInfo













from .ShipmentPromise import ShipmentPromise



from .CartCurrency import CartCurrency





from .SharedCartDetails import SharedCartDetails













from .CartBreakup import CartBreakup



class SharedCart(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
