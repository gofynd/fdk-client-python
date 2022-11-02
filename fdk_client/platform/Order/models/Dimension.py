"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Dimension(BaseSchema):
    #  swagger.json

    
    height = fields.Int(required=False)
    
    width = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    length = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    