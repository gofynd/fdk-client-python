"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BuyRules import BuyRules





from .Ownership2 import Ownership2



from .DiscountRulesApp import DiscountRulesApp





from .AppliedFreeArticles import AppliedFreeArticles













class AppliedPromotion(BaseSchema):
    #  swagger.json

    
    promotion_group = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership2, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
