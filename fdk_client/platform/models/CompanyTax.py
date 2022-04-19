"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class CompanyTax(BaseSchema):
    # CompanyProfile swagger.json

    
    cess = fields.Float(required=False)
    
    rate = fields.Float(required=False)
    
    effective_date = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    

