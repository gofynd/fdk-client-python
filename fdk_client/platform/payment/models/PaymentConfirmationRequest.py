"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .MultiTenderPaymentMethod import MultiTenderPaymentMethod



class PaymentConfirmationRequest(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
