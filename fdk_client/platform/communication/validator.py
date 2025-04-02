

"""Communication Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        



class CommunicationValidator:
    
    
    class sendByCompanyCommunicationSynchronously(BaseSchema):
        
        
        x__application__id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class senByCompanyCommunicationAsynchronously(BaseSchema):
        
        
        x__application__id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class sendByCompanyCommunicationInstantly(BaseSchema):
        
        
        x__application__id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class getSystemNotifications(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Str(required=False)
        
        query = fields.Str(required=False)
         
        
    
    

