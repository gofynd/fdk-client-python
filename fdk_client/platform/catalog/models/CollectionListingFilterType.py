"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CollectionListingFilterType(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
