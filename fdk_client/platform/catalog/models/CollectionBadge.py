"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CollectionBadge(BaseSchema):
    #  swagger.json

    
    color = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
