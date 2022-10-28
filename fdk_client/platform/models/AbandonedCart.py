"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




































































class AbandonedCart(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    coupon = fields.Dict(required=False)
    
    promotion = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    is_archive = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    expire_at = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    cashback = fields.Dict(required=False)
    
    delivery_charges = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    bulk_coupon_discount = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    is_default = fields.Boolean(required=False)
    
    payment_mode = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    checkout_mode = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    cart_value = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    merge_qty = fields.Boolean(required=False)
    
    cod_charges = fields.Dict(required=False)
    
    fynd_credits = fields.Dict(required=False)
    
    payments = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
