"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class Brand(BaseSchema):
    # Order swagger.json

    
    company = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    pickup_location = fields.Str(required=False)
    
    created_on = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    script_last_ran = fields.Str(required=False)
    
    credit_note_expiry_days = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    is_virtual_invoice = fields.Boolean(required=False)
    
    invoice_prefix = fields.Str(required=False)
    
    credit_note_allowed = fields.Boolean(required=False)
    

