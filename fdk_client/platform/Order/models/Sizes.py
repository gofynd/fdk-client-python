"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Sizes(BaseSchema):
    #  swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    
