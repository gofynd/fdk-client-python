"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    

