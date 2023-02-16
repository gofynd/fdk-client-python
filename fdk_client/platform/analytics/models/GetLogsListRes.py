"""analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MkpLogsResp import MkpLogsResp



from .Page import Page



class GetLogsListRes(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(MkpLogsResp, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
