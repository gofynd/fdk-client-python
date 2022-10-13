"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class ShipmentPricesDataSet(BaseSchema):
    # Orders swagger.json

    
    discount = fields.Str(required=False)
    
    refund_credit = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    gst_fee = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    

