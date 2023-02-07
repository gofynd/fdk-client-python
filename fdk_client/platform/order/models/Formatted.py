"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Formatted(BaseSchema):
    #  swagger.json

    
    f_min = fields.Str(required=False)
    
    f_max = fields.Str(required=False)
    
