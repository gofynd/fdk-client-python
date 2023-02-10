"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryValidationResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
