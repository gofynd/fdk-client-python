"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BadRequestResponseGenerateBulkItemParameters import BadRequestResponseGenerateBulkItemParameters




class BadRequestResponseGenerateBulkItem(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    keyword = fields.Str(required=False)
    
    data_path = fields.Str(required=False)
    
    schema_path = fields.Str(required=False)
    
    parameters = fields.Nested(BadRequestResponseGenerateBulkItemParameters, required=False)
    
    message = fields.Str(required=False)
    

