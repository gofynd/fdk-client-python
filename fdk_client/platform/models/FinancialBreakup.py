"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















































class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Int(required=False)
    
    total_units = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    cashback = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    hsn_code = fields.Str(required=False)
    
    gst_fee = fields.Str(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    promotion_effective_discount = fields.Int(required=False)
    
    coupon_value = fields.Int(required=False)
    
    pm_price_split = fields.Dict(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    price_effective = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    transfer_price = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    value_of_good = fields.Int(required=False)
    

