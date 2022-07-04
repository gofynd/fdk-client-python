"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentAllowValue1 import PaymentAllowValue1


class PromotionPaymentModes(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    

