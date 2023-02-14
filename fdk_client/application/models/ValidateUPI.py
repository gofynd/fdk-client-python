"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ValidateUPI(BaseSchema):
    # Payment swagger.json

    
    customer_name = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    upi_vpa = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

