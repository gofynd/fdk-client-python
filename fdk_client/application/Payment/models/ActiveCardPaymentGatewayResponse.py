"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CardPaymentGateway import CardPaymentGateway







class ActiveCardPaymentGatewayResponse(BaseSchema):
    #  swagger.json

    
    cards = fields.Nested(CardPaymentGateway, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
