"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CollectionImage import CollectionImage



from .CollectionImage import CollectionImage



class CollectionBanner(BaseSchema):
    #  swagger.json

    
    landscape = fields.Nested(CollectionImage, required=False)
    
    portrait = fields.Nested(CollectionImage, required=False)
    
