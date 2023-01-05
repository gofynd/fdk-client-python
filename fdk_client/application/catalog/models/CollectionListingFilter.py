"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CollectionListingFilterTag import CollectionListingFilterTag



from .CollectionListingFilterType import CollectionListingFilterType



class CollectionListingFilter(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
