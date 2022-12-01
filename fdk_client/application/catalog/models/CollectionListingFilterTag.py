"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CollectionListingFilterTag(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
