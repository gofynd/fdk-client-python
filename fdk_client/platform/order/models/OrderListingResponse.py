"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page







from .PlatformOrderItems import PlatformOrderItems







class OrderListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    total_count = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    lane = fields.Str(required=False)
    
