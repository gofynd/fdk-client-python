"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .BuyRules import BuyRules

from .DiscountRules import DiscountRules


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    promotion_name = fields.Str(required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    

