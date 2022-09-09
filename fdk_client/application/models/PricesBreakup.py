"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PricesBreakup(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

