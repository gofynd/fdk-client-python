"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .CollectionListingFilter import CollectionListingFilter



from .GetCollectionDetailNest import GetCollectionDetailNest



class GetCollectionListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
