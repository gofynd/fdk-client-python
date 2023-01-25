"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UserCommon(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
