"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TaxInfo(BaseSchema):
    # OrderManage swagger.json

    
    b2b_gstin_number = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    

