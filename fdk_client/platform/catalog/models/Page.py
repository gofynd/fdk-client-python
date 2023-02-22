"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class Page(BaseSchema):
    #  swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    next_id = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
