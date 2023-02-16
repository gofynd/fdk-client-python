"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UpdatedResponse(BaseSchema):
    #  swagger.json

    
    items_not_updated = fields.List(fields.Int(required=False), required=False)
    
    message = fields.Str(required=False)
    
