

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
        
        
        onboarding = fields.Boolean(required=False)
         
        
    
    class getCountry(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        locality_value = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
         
        
    
    


