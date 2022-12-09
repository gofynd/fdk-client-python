"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Identifiers import Identifiers


















































class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    cashback = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    cod_charges = fields.Float(required=False)
    
    total_units = fields.Int(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    transfer_price = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    refund_credit = fields.Float(required=False)
    
    item_name = fields.Str(required=False)
    

