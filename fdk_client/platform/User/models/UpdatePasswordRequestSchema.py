"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UpdatePasswordRequestSchema(BaseSchema):
    #  swagger.json

    
    old_password = fields.Str(required=False)
    
    new_password = fields.Str(required=False)
    
