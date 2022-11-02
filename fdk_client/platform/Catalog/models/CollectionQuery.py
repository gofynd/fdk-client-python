"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CollectionQuery(BaseSchema):
    #  swagger.json

    
    attribute = fields.Str(required=False)
    
    op = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    
