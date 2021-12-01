"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

class UserValidator:
    
    class getCustomers(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class searchUsers(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Dict(required=False)
         
    
    class createUser(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateUser(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
         
    
    class createUserSession(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getPlatformConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updatePlatformConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    