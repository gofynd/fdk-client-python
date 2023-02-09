"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class UserDataInfo(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    avis_user_id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
