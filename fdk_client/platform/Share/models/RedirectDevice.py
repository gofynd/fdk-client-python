"""Share Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class RedirectDevice(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
