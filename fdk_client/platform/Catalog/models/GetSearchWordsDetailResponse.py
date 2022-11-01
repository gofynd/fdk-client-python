"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetSearchWordsData import GetSearchWordsData



from .Page import Page



class GetSearchWordsDetailResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(GetSearchWordsData, required=False)
    
    page = fields.Nested(Page, required=False)
    
