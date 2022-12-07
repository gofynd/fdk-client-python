"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PaymentMethods import PaymentMethods







class PaymentInfo(BaseSchema):
    #  swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethods, required=False), required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    