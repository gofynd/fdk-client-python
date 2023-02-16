"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class AndroidPathsRes(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
