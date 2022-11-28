"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CartBreakup import CartBreakup

from .CartCurrency import CartCurrency



from .PaymentSelectionLock import PaymentSelectionLock





from .ShipmentPromise import ShipmentPromise

from .ShipmentResponse import ShipmentResponse












class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    error = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    comment = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    coupon_text = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    last_modified = fields.Str(required=False)
    

