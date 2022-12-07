"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PaymentOptionAndFlow import PaymentOptionAndFlow



class PaymentModeRouteResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    