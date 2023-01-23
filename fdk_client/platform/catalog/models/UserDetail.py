"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class UserDetail(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    
    username = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
