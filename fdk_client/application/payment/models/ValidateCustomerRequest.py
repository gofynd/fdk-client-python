"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




















class ValidateCustomerRequest(BaseSchema):
    #  swagger.json

    
    transaction_amount_in_paise = fields.Int(required=False)
    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    merchant_params = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
    payload = fields.Str(required=False)
    
