"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .BalanceDetails import BalanceDetails







class CreditSummary(BaseSchema):
    #  swagger.json

    
    status_message = fields.Str(required=False)
    
    balance = fields.Nested(BalanceDetails, required=False)
    
    status = fields.Str(required=False)
    
    merchant_customer_ref_id = fields.Str(required=False)
    
