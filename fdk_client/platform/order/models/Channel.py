"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Channel(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
