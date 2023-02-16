"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class UpdateUserRequestSchema(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
