"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CollectionQuery import CollectionQuery



from .ItemQueryForUserCollection import ItemQueryForUserCollection



class CollectionItemRequest(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    item = fields.List(fields.Nested(ItemQueryForUserCollection, required=False), required=False)
    
