"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CardPaymentGateway import CardPaymentGateway



class ActiveCardPaymentGatewayResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    cards = fields.Nested(CardPaymentGateway, required=False)
    