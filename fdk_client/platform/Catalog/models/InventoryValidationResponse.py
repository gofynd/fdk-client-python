"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryValidationResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
