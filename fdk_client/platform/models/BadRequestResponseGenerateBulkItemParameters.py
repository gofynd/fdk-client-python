"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BadRequestResponseGenerateBulkItemParameters(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    missing_property = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

