"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UpdateUserGroupSchema(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    