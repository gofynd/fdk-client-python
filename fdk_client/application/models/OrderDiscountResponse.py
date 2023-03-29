"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DiscountProperties import DiscountProperties

from .DiscountProperties import DiscountProperties

from .OrderDiscountRuleBucket import OrderDiscountRuleBucket


class OrderDiscountResponse(BaseSchema):
    # Rewards swagger.json

    
    order_amount = fields.Float(required=False)
    
    points = fields.Float(required=False)
    
    discount = fields.Nested(DiscountProperties, required=False)
    
    base_discount = fields.Nested(DiscountProperties, required=False)
    
    applied_rule_bucket = fields.Nested(OrderDiscountRuleBucket, required=False)
    

