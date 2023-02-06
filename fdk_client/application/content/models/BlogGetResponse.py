"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BlogSchema import BlogSchema



from .Page import Page



class BlogGetResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
