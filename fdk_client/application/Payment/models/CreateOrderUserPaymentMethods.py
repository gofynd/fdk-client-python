"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PaymentMethodsMeta import PaymentMethodsMeta





class CreateOrderUserPaymentMethods(BaseSchema):
    #  swagger.json

    
    mode = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMeta, required=False)
    
    name = fields.Str(required=False)
    
