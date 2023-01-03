"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class InventoryPage(BaseSchema):
    #  swagger.json

    
    next_id = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
