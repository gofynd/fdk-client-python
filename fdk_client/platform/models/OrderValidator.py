"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderValidator:
    
    class bulkActionProcessXlsxFile(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        url = fields.Str(required=False)
         
    
    class bulkActionDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
    