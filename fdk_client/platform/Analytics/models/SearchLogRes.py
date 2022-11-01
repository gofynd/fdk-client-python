"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LogInfo import LogInfo



from .Page import Page



class SearchLogRes(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(LogInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
