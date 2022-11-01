"""Rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class OrderDiscountRequest(BaseSchema):
    #  swagger.json

    
    currency = fields.Str(required=False)
    
    order_amount = fields.Float(required=False)
    
