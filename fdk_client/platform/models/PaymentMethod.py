"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class PaymentMethod(BaseSchema):
    # Order swagger.json

    
    collect_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    transaction_data = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

