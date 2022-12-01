"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .RootPaymentMode import RootPaymentMode



from .PaymentFlow import PaymentFlow



class PaymentOptionAndFlow(BaseSchema):
    #  swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    
