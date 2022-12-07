"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OpenApiFiles(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    