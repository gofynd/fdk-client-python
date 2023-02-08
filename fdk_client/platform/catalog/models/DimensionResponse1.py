"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class DimensionResponse1(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
