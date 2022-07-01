"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ShipmentResponse import ShipmentResponse



from .CartCurrency import CartCurrency





from .PaymentSelectionLock import PaymentSelectionLock





from .CartBreakup import CartBreakup









from .ShipmentPromise import ShipmentPromise




class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Int(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    uid = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    comment = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    id = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    error = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    

