"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class StatusSuccessResponse(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    

