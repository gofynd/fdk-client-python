"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class DimensionResponse1(BaseSchema):
    #  swagger.json

    
    height = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    length = fields.Float(required=False)
    
