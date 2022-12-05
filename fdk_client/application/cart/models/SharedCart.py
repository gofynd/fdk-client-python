"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .PaymentSelectionLock import PaymentSelectionLock



from .CartBreakup import CartBreakup











from .CartCurrency import CartCurrency











from .CartProductInfo import CartProductInfo



from .SharedCartDetails import SharedCartDetails



from .ShipmentPromise import ShipmentPromise





class SharedCart(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
