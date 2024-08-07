

"""Lead Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
        
    
    
    
        
    
    
        

class LeadValidator:
    
    
    class getTicket(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class createHistory(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class createTicket(BaseSchema):
        
        pass 
        
    
    class getCustomForm(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class submitCustomForm(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    


