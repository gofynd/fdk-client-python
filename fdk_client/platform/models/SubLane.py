"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class SubLane(BaseSchema):
    # Orders swagger.json

    
    text = fields.Str(required=False)
    
    index = fields.Int(required=False)
    
    next_state = fields.List(fields.Str(required=False), required=False)
    
    current_state = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Str(required=False)
    
    total_shipments = fields.Int(required=False)
    
