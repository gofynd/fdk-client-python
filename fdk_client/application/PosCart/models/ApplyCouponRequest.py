"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ApplyCouponRequest(BaseSchema):
    #  swagger.json

    
    coupon_code = fields.Str(required=False)
    
