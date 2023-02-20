"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ApplyCouponRequest(BaseSchema):
    #  swagger.json

    
    coupon_code = fields.Str(required=False)
    
