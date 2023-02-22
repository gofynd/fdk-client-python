"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .DiscountRulesApp import DiscountRulesApp



from .AppliedFreeArticles import AppliedFreeArticles







from .BuyRules import BuyRules





from .Ownership import Ownership











class AppliedPromotion(BaseSchema):
    #  swagger.json

    
    promo_id = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
