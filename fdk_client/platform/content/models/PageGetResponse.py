"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PageSchema import PageSchema



from .Page import Page



class PageGetResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
