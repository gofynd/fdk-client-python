"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class EInvoice(BaseSchema):
    # Order swagger.json

    
    irn = fields.Str(required=False)
    
    signed_invoice = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    
    acknowledge_no = fields.Int(required=False)
    
    signed_qr_code = fields.Str(required=False)
    
    error_code = fields.Str(required=False)
    
    acknowledge_date = fields.Str(required=False)
    

