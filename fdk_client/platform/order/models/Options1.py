"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Options1(BaseSchema):
    #  swagger.json

    
    value = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
