"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ArchiveUserRequestSchema(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
