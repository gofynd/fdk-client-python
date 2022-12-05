"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class QuantityBase(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    
