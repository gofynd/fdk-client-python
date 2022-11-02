"""Rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ItemsData(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
