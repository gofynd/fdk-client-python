"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class Page(BaseSchema):
    #  swagger.json

    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
