"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BuyRules import BuyRules











from .DiscountRules import DiscountRules







class AppliedPromos(BaseSchema):
    #  swagger.json

    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    article_quantity = fields.Int(required=False)
    
