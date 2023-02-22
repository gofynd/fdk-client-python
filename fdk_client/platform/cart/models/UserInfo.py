"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class UserInfo(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
