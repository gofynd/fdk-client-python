"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Dimensions(BaseSchema):
    #  swagger.json

    
    width = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    length = fields.Int(required=False)
    
    height = fields.Int(required=False)
    
