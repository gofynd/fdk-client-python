"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EInvoicePortalDetails(BaseSchema):
    # Order swagger.json

    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    user = fields.Str(required=False)
    

