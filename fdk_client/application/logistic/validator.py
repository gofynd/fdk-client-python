

"""Logistic Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
    
    
        

class LogisticValidator:
    
    
    class getTatProduct(BaseSchema):
        
        pass 
        
    
    class getPincodeZones(BaseSchema):
        
        pass 
        
    
    class getPincodeCity(BaseSchema):
        
        
        pincode = fields.Str(required=False)
         
        
    
    


