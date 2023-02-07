"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class SetCODForUserRequest(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    merchant_user_id = fields.Str(required=False)
    
    mobileno = fields.Str(required=False)
    
