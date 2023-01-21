"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Meta import Meta


class PaymentMethod(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    payment = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    

