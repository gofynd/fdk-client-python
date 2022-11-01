"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Debug(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
