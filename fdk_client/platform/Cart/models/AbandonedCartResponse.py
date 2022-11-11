"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Page import Page



from .AbandonedCart import AbandonedCart



class AbandonedCartResponse(BaseSchema):
    #  swagger.json

    
    result = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
