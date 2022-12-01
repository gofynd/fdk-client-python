"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




















class ErrorDescription(BaseSchema):
    #  swagger.json

    
    merchant_name = fields.Str(required=False)
    
    invalid_id = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    expired = fields.Boolean(required=False)
    
    msg = fields.Str(required=False)
    
    cancelled = fields.Boolean(required=False)
    
    payment_transaction_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
