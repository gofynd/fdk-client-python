"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class UpdateCartPaymentRequest(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    