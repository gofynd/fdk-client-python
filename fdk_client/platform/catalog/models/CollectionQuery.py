"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CollectionQuery(BaseSchema):
    #  swagger.json

    
    value = fields.List(fields.Raw(required=False), required=False)
    
    op = fields.Str(required=False)
    
    attribute = fields.Str(required=False)
    
