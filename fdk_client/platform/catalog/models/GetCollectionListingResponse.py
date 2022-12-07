"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetCollectionDetailNest import GetCollectionDetailNest



from .CollectionListingFilter import CollectionListingFilter



from .Page import Page



class GetCollectionListingResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    page = fields.Nested(Page, required=False)
    