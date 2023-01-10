"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PageResponse(BaseSchema):
    #  swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Str(required=False)
    
