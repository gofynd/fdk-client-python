"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CartProductInfo import CartProductInfo

from .PaymentSelectionLock import PaymentSelectionLock

from .CartCurrency import CartCurrency

from .ShipmentPromise import ShipmentPromise







from .CartBreakup import CartBreakup












class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    comment = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    

