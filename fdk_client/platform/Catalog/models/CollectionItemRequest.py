"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemQueryForUserCollection import ItemQueryForUserCollection





from .CollectionQuery import CollectionQuery



class CollectionItemRequest(BaseSchema):
    #  swagger.json

    
    item = fields.List(fields.Nested(ItemQueryForUserCollection, required=False), required=False)
    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
