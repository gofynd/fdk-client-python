"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentPromise import ShipmentPromise

from .CartProductInfo import CartProductInfo











from .CartBreakup import CartBreakup









from .PaymentSelectionLock import PaymentSelectionLock





from .CartCurrency import CartCurrency

from .SharedCartDetails import SharedCartDetails




class SharedCart(BaseSchema):
    # Cart swagger.json

    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    coupon_text = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    gstin = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    message = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    

