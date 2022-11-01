"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ValidateCustomerRequest(BaseSchema):
    #  swagger.json

    
    merchant_params = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    payload = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
