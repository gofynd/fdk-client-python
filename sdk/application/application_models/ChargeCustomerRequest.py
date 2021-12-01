"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ChargeCustomerRequest(BaseSchema):

    
    amount = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False)
    

