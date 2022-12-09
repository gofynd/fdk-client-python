"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EInvoicePortalDetails(BaseSchema):
    # Orders swagger.json

    
    username = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    password = fields.Str(required=False)
    

