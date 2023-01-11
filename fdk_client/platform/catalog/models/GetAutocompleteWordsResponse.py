"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetAutocompleteWordsData import GetAutocompleteWordsData



from .Page import Page



class GetAutocompleteWordsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetAutocompleteWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
