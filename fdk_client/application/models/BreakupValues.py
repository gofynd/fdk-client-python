"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class BreakupValues(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    display = fields.Str(required=False)
    

