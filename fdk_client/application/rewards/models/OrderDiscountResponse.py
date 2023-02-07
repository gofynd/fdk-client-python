"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .DiscountProperties import DiscountProperties



from .DiscountProperties import DiscountProperties



from .OrderDiscountRuleBucket import OrderDiscountRuleBucket



class OrderDiscountResponse(BaseSchema):
    #  swagger.json

    
    order_amount = fields.Float(required=False)
    
    points = fields.Float(required=False)
    
    discount = fields.Nested(DiscountProperties, required=False)
    
    base_discount = fields.Nested(DiscountProperties, required=False)
    
    applied_rule_bucket = fields.Nested(OrderDiscountRuleBucket, required=False)
    
