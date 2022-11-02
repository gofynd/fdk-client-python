"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
























class Coupon(BaseSchema):
    #  swagger.json

    
    coupon_code = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    expires_on = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    title = fields.Str(required=False)
    