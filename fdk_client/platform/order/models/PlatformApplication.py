"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PlatformApplication(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    