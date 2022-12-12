"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Tax(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Dict(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    tax_exempt = fields.Boolean(required=False)
    

