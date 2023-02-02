"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetInventories import GetInventories



from .Page import Page



class GetInventoriesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetInventories, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
