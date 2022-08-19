"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SignedBadRequestResponse(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    

