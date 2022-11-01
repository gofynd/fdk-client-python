"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class BlitzkriegApiErrorSchema(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
