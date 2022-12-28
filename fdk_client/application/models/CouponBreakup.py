"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_type = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    

