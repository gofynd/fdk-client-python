"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PaymentSelectionLock import PaymentSelectionLock







from .CartCurrency import CartCurrency



from .ShipmentPromise import ShipmentPromise















from .CartBreakup import CartBreakup





from .ShipmentResponse import ShipmentResponse











class CartShipmentsResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    uid = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
