"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




































class Prices(BaseSchema):
    #  swagger.json

    
    cod_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
