"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class SellerAddress(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    name = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
