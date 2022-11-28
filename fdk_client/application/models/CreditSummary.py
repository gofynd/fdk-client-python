"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BalanceDetails import BalanceDetails

from .BalanceDetails import BalanceDetails




class CreditSummary(BaseSchema):
    # Payment swagger.json

    
    credit_line_id = fields.Str(required=False)
    
    merchant_customer_ref_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    status_message = fields.Str(required=False)
    
    balance = fields.Nested(BalanceDetails, required=False)
    
    amount_available = fields.Nested(BalanceDetails, required=False)
    
    buyer_status = fields.Str(required=False)
    

