"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class OrderListingResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    total_count = fields.Int(required=False)
    
    lane = fields.Str(required=False)
    

