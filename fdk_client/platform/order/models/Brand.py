"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class Brand(BaseSchema):
    #  swagger.json

    
    brand_name = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    
    script_last_ran = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    pickup_location = fields.Str(required=False)
    
    credit_note_expiry_days = fields.Int(required=False)
    
    credit_note_allowed = fields.Boolean(required=False)
    
    created_on = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    is_virtual_invoice = fields.Boolean(required=False)
    
    start_date = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    invoice_prefix = fields.Str(required=False)
    