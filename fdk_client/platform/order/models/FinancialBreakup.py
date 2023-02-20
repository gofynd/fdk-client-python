"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .Identifier import Identifier













































class FinancialBreakup(BaseSchema):
    #  swagger.json

    
    value_of_good = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    transfer_price = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    price_marked = fields.Int(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    total_units = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    gst_fee = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    refund_credit = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
