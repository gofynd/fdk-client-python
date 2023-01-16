"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PaymentAllowValue1 import PaymentAllowValue1





class PromotionPaymentModes(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
