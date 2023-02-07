"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Options(BaseSchema):
    #  swagger.json

    
    value = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
