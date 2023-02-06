"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BrandMeta(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
