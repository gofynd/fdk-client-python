

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
        
    
    class getLocations(BaseSchema):
        
        
        x__application__id = fields.Str(required=False)
        
        x__application__data = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        pincode = fields.Int(required=False)
        
        sector = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        onboarding = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getCountry(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        locality_value = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
         
        
    
    class validateAddress(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
        
        template_name = fields.Str(required=False)
         
        
    
    


