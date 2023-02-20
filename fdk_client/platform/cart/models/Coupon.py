"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























class Coupon(BaseSchema):
    #  swagger.json

    
    minimum_cart_value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
