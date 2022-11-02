"""Rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class PageData(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
