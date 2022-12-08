"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentMethods import PaymentMethods


class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    source = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethods, required=False), required=False)
    

