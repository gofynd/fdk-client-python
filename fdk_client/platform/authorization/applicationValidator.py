

"""Authorization Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
        
        
        

class AuthorizationValidator:
    
    
    class getApplicationStaffList(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        order_incent = fields.Boolean(required=False)
        
        ordering_store = fields.Int(required=False)
        
        user = fields.Str(required=False)
        
        user_name = fields.Str(required=False)
         
        
    
    

