"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderPrices import OrderPrices









































from .OrderTaxDetails import OrderTaxDetails



















from .OrderMeta import OrderMeta




class OrderObj(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(OrderPrices, required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    raw_user_agent = fields.Str(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    payment_mode_id = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    headers = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    ordering_channel_logo = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    user_id = fields.Int(required=False)
    
    mongo_cart_id = fields.Raw(required=False)
    
    source = fields.Str(required=False)
    
    created_time = fields.Int(required=False)
    
    o_id = fields.Int(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    tax_details = fields.Nested(OrderTaxDetails, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    total_order_value = fields.Float(required=False)
    
    affiliate_order_date = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    cashback_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    cashback_applied = fields.Float(required=False)
    

