"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SlideshowSchema import SlideshowSchema



from .Page import Page



class SlideshowGetResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(SlideshowSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
