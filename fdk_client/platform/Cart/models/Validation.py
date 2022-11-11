"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Validation(BaseSchema):
    #  swagger.json

    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    user_registered_after = fields.Str(required=False)
    
    anonymous = fields.Boolean(required=False)
    
