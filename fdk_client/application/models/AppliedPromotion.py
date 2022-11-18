"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AppliedFreeArticles import AppliedFreeArticles









from .BuyRules import BuyRules





from .DiscountRules import DiscountRules


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    article_quantity = fields.Int(required=False)
    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    

