"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LandingPageSchema import LandingPageSchema



from .Page import Page



class LandingPageGetResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(LandingPageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
