"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentMeta import PaymentMeta










class PaymentMethod(BaseSchema):
    # Cart swagger.json

    
    payment_meta = fields.Nested(PaymentMeta, required=False)
    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    

