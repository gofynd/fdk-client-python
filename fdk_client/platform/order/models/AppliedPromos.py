"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DiscountRules import DiscountRules





from .BuyRules import BuyRules











class AppliedPromos(BaseSchema):
    #  swagger.json

    
    promo_id = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
