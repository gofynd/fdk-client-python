"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class NetQuantityResponse(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
