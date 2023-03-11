

"""Logistic Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
        
    
    
    

class LogisticValidator:
    
    
    class getPincodeCity(BaseSchema):
        
        
        pincode = fields.Str(required=False)
        
        country_code = fields.Str(required=False)
         
        
    
    class getTatProduct(BaseSchema):
        
        pass 
        
    
    class getAllCountries(BaseSchema):
        
        pass 
        
    
    class getPincodeZones(BaseSchema):
        
        pass 
        
    
    


