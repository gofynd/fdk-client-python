"""common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Scopes(BaseSchema):
    #  swagger.json

    
    permissions = fields.List(fields.Str(required=False), required=False)
    
