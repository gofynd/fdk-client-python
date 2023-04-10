"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TaxDetails(BaseSchema):
    # Order swagger.json

    
    gstin = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    

