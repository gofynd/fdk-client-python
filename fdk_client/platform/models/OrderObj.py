"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .OrderMeta import OrderMeta





from .OrderTaxDetails import OrderTaxDetails

from .OrderPrices import OrderPrices










































class OrderObj(BaseSchema):
    # Order swagger.json

    
    collect_by = fields.Str(required=False)
    
    created_time = fields.Int(required=False)
    
    o_id = fields.Int(required=False)
    
    headers = fields.Dict(required=False)
    
    affiliate_order_date = fields.Str(required=False)
    
    ordering_channel_logo = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    order_value = fields.Float(required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    raw_user_agent = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    tax_details = fields.Nested(OrderTaxDetails, required=False)
    
    prices = fields.Nested(OrderPrices, required=False)
    
    delivery_charges = fields.Float(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    cashback_value = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    transaction_id = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    user_id = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    payment_mode_id = fields.Int(required=False)
    
    refund_by = fields.Str(required=False)
    
    mongo_cart_id = fields.Raw(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    total_order_value = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    source = fields.Str(required=False)
    

