"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class TransactionData(BaseSchema):
    # Order swagger.json

    
    entity = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    terminal_id = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    unique_reference_number = fields.Str(required=False)
    
    amount_paid = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    

