"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PlatformOrderItems import PlatformOrderItems

from .Page import Page




class OrderListingResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    total_count = fields.Int(required=False)
    
    lane = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    

