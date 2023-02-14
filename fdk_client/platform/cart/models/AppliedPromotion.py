"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Ownership2 import Ownership2











from .BuyRules import BuyRules



from .AppliedFreeArticles import AppliedFreeArticles



from .DiscountRulesApp import DiscountRulesApp







class AppliedPromotion(BaseSchema):
    #  swagger.json

    
    offer_text = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    ownership = fields.Nested(Ownership2, required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
