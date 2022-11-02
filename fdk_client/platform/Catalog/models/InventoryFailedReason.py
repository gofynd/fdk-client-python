"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryFailedReason(BaseSchema):
    #  swagger.json

    
    errors = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
