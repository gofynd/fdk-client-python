"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .PaymentAllowValue import PaymentAllowValue



class PaymentModes(BaseSchema):
    #  swagger.json

    
    types = fields.List(fields.Str(required=False), required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    