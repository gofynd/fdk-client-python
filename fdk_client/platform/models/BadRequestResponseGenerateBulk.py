"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BadRequestResponseGenerateBulkItem import BadRequestResponseGenerateBulkItem


class BadRequestResponseGenerateBulk(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.List(fields.Nested(BadRequestResponseGenerateBulkItem, required=False), required=False)
    

