"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetSearchWordsData import GetSearchWordsData



from .Page import Page



class GetSearchWordsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
