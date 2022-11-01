"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ConfigPage(BaseSchema):
    #  swagger.json

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    
