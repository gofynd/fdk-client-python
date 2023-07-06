

"""Logistic Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
    
    
    
    
    
        
    
    
        
    
    
        
        

class LogisticValidator:
    
    
    class getPincodeCity(BaseSchema):
        
        
        pincode = fields.Str(required=False)
         
        
    
    class getTatProduct(BaseSchema):
        
        pass 
        
    
    class getAllCountries(BaseSchema):
        
        pass 
        
    
    class getPincodeZones(BaseSchema):
        
        pass 
        
    
    class getOptimalLocations(BaseSchema):
        
        pass 
        
    
    class getCountries(BaseSchema):
        
        pass 
        
    
    class getCountry(BaseSchema):
        
        
        uid = fields.Str(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        region = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        region = fields.Str(required=False)
        
        value = fields.Str(required=False)
         
        
    
    


