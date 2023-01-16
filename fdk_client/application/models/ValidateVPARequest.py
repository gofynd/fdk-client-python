"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ValidateVPARequest(BaseSchema):
    # Payment swagger.json

    
    upi_vpa = fields.Str(required=False)
    

