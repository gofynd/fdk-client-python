"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PlatformOrderItems import PlatformOrderItems









from .Page import Page



class OrderListingResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    message = fields.Str(required=False)
    
    lane = fields.Str(required=False)
    
    total_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    
