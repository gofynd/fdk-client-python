"""Rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderDiscountRuleBucket import OrderDiscountRuleBucket



from .DiscountProperties import DiscountProperties



from .DiscountProperties import DiscountProperties







class OrderDiscountResponse(BaseSchema):
    #  swagger.json

    
    applied_rule_bucket = fields.Nested(OrderDiscountRuleBucket, required=False)
    
    base_discount = fields.Nested(DiscountProperties, required=False)
    
    discount = fields.Nested(DiscountProperties, required=False)
    
    order_amount = fields.Float(required=False)
    
    points = fields.Float(required=False)
    
