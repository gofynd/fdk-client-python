

"""Lead Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
        
                
from .models.PriorityEnum import PriorityEnum

        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        

class LeadValidator:
    
    
    class getTickets(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Nested(PriorityEnum, required=False)
        
        category = fields.Str(required=False)
         
        
    
    class getTicket(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class editTicket(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createHistory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getTicketHistory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getCustomForm(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class editCustomForm(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getCustomForms(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createCustomForm(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getTokenForVideoRoom(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
        
    
    class getVideoParticipants(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
        
    
    class openVideoRoom(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class closeVideoRoom(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
        
    
    

