"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Timestamp(BaseSchema):
    #  swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
