"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class DimensionResponse(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    height = fields.Float(required=False)
    
