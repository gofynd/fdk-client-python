"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BulkListBadRequestResponse(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    

