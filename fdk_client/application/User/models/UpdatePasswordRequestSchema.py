"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class UpdatePasswordRequestSchema(BaseSchema):
    #  swagger.json

    
    old_password = fields.Str(required=False)
    
    new_password = fields.Str(required=False)
    
