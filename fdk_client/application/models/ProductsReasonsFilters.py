"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
