"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CollectionListingFilter import CollectionListingFilter



from .Page import Page



from .GetCollectionDetailNest import GetCollectionDetailNest



class GetCollectionListingResponse(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
