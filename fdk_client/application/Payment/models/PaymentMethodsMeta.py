"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PaymentMethodsMeta(BaseSchema):
    #  swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
