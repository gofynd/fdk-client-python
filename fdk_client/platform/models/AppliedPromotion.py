"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AppliedFreeArticles import AppliedFreeArticles



from .BuyRules import BuyRules







from .DiscountRulesApp import DiscountRulesApp


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    promotion_group = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Int(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    

