"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Validation(BaseSchema):
    #  swagger.json

    
    user_registered_after = fields.Str(required=False)
    
    anonymous = fields.Boolean(required=False)
    
    app_id = fields.List(fields.Str(required=False), required=False)
    
