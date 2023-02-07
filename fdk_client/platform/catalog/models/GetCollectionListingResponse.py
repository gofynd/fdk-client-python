"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CollectionListingFilter import CollectionListingFilter



from .GetCollectionDetailNest import GetCollectionDetailNest



from .Page import Page



class GetCollectionListingResponse(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
