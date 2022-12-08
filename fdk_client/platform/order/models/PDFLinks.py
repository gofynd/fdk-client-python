"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class PDFLinks(BaseSchema):
    #  swagger.json

    
    invoice_a4 = fields.Str(required=False)
    
    label_pos = fields.Str(required=False)
    
    invoice = fields.Str(required=False)
    
    invoice_pos = fields.Str(required=False)
    
    invoice_a6 = fields.Str(required=False)
    
    credit_note_url = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    b2b = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    
    label_a6 = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    label_a4 = fields.Str(required=False)
    
    po_invoice = fields.Str(required=False)
    
