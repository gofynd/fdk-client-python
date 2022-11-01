"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AbandonCartsDetail import AbandonCartsDetail





from .Page import Page



class AbandonCartsList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AbandonCartsDetail, required=False), required=False)
    
    cart_total = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
