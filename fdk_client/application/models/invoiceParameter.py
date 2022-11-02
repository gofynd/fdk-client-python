"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class invoiceParameter(BaseSchema):
    # Order swagger.json

    
    document_type = fields.Str(required=False)
    
    expires_in = fields.Int(required=False)
    

