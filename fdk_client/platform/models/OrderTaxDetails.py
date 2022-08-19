"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OrderTaxDetails(BaseSchema):
    # Order swagger.json

    
    gstin = fields.Str(required=False)
    
    b2b_gstin_number = fields.Str(required=False)
    

