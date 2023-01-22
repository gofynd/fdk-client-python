"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class Page(BaseSchema):
    #  swagger.json

    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
