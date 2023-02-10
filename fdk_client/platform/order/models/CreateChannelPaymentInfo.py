"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PaymentMethods import PaymentMethods







class CreateChannelPaymentInfo(BaseSchema):
    #  swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethods, required=False), required=False)
    
    source = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
