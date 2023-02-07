"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PaymentMethod import PaymentMethod





class PaymentInfo(BaseSchema):
    #  swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    primary_mode = fields.Str(required=False)
    
