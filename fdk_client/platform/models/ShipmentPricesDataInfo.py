"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class ShipmentPricesDataInfo(BaseSchema):
    # Orders swagger.json

    
    refund_credit = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    coupon_value = fields.Str(required=False)
    
    cashback = fields.Int(required=False)
    
    refund_amount = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    

