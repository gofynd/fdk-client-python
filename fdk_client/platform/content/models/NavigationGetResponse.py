"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .NavigationSchema import NavigationSchema



from .Page import Page



class NavigationGetResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
