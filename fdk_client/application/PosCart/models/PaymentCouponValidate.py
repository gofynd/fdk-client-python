"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CouponValidity import CouponValidity







class PaymentCouponValidate(BaseSchema):
    #  swagger.json

    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    