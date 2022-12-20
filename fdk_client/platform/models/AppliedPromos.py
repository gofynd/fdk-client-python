"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DiscountRules import DiscountRules

from .BuyRules import BuyRules












class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    

