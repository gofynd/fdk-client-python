"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ChargeCustomerRequest(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    transaction_token = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
