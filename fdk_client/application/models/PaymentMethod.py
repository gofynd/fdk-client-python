"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .PaymentMeta import PaymentMeta


class PaymentMethod(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    payment = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    payment_meta = fields.Nested(PaymentMeta, required=False)
    

