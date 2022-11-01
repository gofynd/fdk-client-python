"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .ItemTotal import ItemTotal



class PlatformOrderPage(BaseSchema):
    #  swagger.json

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    item_total = fields.Nested(ItemTotal, required=False)
    
