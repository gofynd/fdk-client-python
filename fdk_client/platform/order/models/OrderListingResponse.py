"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Page import Page



from .PlatformOrderItems import PlatformOrderItems







class OrderListingResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    total_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    message = fields.Str(required=False)
    
    lane = fields.Str(required=False)
    
