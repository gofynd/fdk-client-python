

"""Lead Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
        
        
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        

class LeadValidator:
    
    
    class getTickets(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Str(required=False)
        
        category = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createTicket(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getTicket(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class editTicket(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createHistory(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getTicketHistory(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getGeneralConfig(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    

