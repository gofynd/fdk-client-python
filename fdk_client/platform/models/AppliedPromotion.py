"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DiscountRules import DiscountRules







from .AppliedFreeArticles import AppliedFreeArticles





from .BuyRules import BuyRules






class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    
    promotion_name = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promo_id = fields.Str(required=False)
    

