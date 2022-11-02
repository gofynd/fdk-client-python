"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PlatformEmail(BaseSchema):
    #  swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    