"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PlatformUserDetails(BaseSchema):
    # Order swagger.json

    
    platform_user_employee_code = fields.Str(required=False)
    
    platform_user_last_name = fields.Str(required=False)
    
    platform_user_first_name = fields.Str(required=False)
    
    platform_user_id = fields.Str(required=False)
    

