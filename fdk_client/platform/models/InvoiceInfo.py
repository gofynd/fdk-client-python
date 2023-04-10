"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class InvoiceInfo(BaseSchema):
    # Order swagger.json

    
    label_url = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    store_invoice_id = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    

