"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderInvoiceEngineValidator:
    
    class generateBulkPackageLabel(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class generateBulkBoxLabel(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getLabelStatus(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
    
    class getLabelPresignedURL(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
    