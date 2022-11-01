"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CollectionListingFilterType import CollectionListingFilterType



from .CollectionListingFilterTag import CollectionListingFilterTag



class CollectionListingFilter(BaseSchema):
    #  swagger.json

    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
