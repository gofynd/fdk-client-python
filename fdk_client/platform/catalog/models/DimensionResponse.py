"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class DimensionResponse(BaseSchema):
    #  swagger.json

    
    width = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
