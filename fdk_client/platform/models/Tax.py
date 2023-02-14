"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Tax(BaseSchema):
    # Order swagger.json

    
    amount = fields.Dict(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    rate = fields.Float(required=False)
    
    name = fields.Str(required=False)
    

