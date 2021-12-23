"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    merchant_params = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    payload = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    

