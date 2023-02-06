"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class SubLane(BaseSchema):
    # Order swagger.json

    
    actions = fields.List(fields.Dict(required=False), required=False)
    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    index = fields.Int(required=False)
    
    total_items = fields.Int(required=False)
    

