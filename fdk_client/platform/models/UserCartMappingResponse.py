"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ShipmentPromise import ShipmentPromise





from .CartProductInfo import CartProductInfo







from .CartBreakup import CartBreakup



from .PaymentSelectionLock import PaymentSelectionLock



from .UserInfo import UserInfo

from .CartCurrency import CartCurrency










class UserCartMappingResponse(BaseSchema):
    # Cart swagger.json

    
    pan_config = fields.Dict(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    user = fields.Nested(UserInfo, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    pan_no = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    

