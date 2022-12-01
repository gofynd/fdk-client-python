"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class OrderDiscountRuleBucket(BaseSchema):
    #  swagger.json

    
    high = fields.Float(required=False)
    
    low = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    value_type = fields.Str(required=False)
    
