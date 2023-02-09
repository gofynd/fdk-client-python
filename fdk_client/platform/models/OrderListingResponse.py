"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Page import Page





from .PlatformOrderItems import PlatformOrderItems




class OrderListingResponse(BaseSchema):
    # Orders swagger.json

    
    lane = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    total_count = fields.Int(required=False)
    

