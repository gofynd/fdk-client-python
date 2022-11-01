"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Medium(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    
