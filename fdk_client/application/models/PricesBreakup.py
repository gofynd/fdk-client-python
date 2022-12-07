"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PricesBreakup(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

