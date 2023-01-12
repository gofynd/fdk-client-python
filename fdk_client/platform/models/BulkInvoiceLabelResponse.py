"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class BulkInvoiceLabelResponse(BaseSchema):
    # Order swagger.json

    
    label = fields.Dict(required=False)
    
    store_code = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    store_id = fields.Str(required=False)
    
    invoice_status = fields.Str(required=False)
    
    do_invoice_label_generated = fields.Boolean(required=False)
    
    store_name = fields.Str(required=False)
    
    invoice = fields.Dict(required=False)
    
    batch_id = fields.Str(required=False)
    

