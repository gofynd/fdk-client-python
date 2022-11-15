"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RevenueTaxDetail(BaseSchema):
    # Cart swagger.json

    
    tax_type = fields.Str(required=False)
    
    tax_percentage = fields.Float(required=False)
    

