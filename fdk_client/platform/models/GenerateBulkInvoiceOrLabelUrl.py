"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GenerateBulkInvoiceOrLabelUrl(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    uid = fields.Str(required=False)
    
    document_type = fields.Str(required=False)
    
    batch_id = fields.Float(required=False)
    

