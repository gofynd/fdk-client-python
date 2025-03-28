

"""Authorization Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        

class AuthorizationValidator:
    
    
    class createOrganizationClient(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getOrganizationClientList(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
         
        
    
    class getOrganizationClientById(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        client_id = fields.Str(required=False)
         
        
    
    class updateOrganizationClientById(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        client_id = fields.Str(required=False)
         
        
    
    class deleteOrganizationOAuthClientById(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        client_id = fields.Str(required=False)
         
        
    
    

