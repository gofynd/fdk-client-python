"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .EditProfileMobileSchema import EditProfileMobileSchema


















class EditProfileRequestSchema(BaseSchema):

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Nested(EditProfileMobileSchema, required=False)
    
    country_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    dob = fields.Str(required=False)
    
    profile_pic_url = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    

