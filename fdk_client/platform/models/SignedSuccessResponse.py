"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SignedSuccessResponse(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    uid = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    

