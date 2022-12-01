"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ChargeCustomerRequest(BaseSchema):
    #  swagger.json

    
    verified = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False)
    
