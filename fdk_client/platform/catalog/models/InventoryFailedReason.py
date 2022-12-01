"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryFailedReason(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Str(required=False)
    
