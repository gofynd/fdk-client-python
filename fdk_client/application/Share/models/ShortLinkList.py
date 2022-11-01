"""Share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ShortLinkRes import ShortLinkRes



from .Page import Page



class ShortLinkList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ShortLinkRes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
