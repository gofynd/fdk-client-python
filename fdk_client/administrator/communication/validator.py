

"""Communication Administrator Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..AdministratorModel import BaseSchema



    
    

class CommunicationValidator:
    
    
    class sendSellerCommunicationSynchronously(BaseSchema):
        
        pass 
        
    
    class sendSellerCommunicationAsynchronously(BaseSchema):
        
        pass 
        
    
    


