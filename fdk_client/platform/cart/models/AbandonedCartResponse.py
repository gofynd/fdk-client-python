"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page







from .AbandonedCart import AbandonedCart





class AbandonedCartResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    result = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
