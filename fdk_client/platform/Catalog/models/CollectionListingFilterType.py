"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CollectionListingFilterType(BaseSchema):
    #  swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    