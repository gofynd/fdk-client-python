"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DiscountRulesApp import DiscountRulesApp



from .BuyRules import BuyRules











from .AppliedFreeArticles import AppliedFreeArticles




class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    
    article_quantity = fields.Int(required=False)
    

