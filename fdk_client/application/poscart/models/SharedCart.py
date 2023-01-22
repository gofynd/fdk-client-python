"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















from .CartBreakup import CartBreakup









from .CartCurrency import CartCurrency









from .CartProductInfo import CartProductInfo



from .ShipmentPromise import ShipmentPromise



from .PaymentSelectionLock import PaymentSelectionLock





from .SharedCartDetails import SharedCartDetails



class SharedCart(BaseSchema):
    #  swagger.json

    
    cart_id = fields.Int(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    