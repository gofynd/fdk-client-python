"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class CouponBreakup(BaseSchema):
    #  swagger.json

    
    coupon_value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
