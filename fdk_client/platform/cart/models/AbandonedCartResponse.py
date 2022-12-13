"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .AbandonedCart import AbandonedCart



from .Page import Page







class AbandonedCartResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    
