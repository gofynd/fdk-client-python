"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GenericDTO(BaseSchema):
    #  swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
