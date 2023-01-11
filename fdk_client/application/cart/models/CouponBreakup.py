"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






























class CouponBreakup(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
