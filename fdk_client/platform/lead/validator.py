

"""Lead Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
        
        
                
from .models import PriorityEnum

        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        



class LeadValidator:
    
    
    class getPlatformTickets(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Nested(PriorityEnum, required=False)
        
        category = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createTicket(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getPlatformTicket(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class editPlatformTicket(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createPlatformTicketHistory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getPlatformTicketHistory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getFeedbacks(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class submitFeedback(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getGeneralConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    

