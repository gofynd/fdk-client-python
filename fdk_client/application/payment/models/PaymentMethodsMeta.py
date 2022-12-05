"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PaymentMethodsMeta(BaseSchema):
    #  swagger.json

    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
