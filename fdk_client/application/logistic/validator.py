

"""Logistic Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        

class LogisticValidator:
    
    
    class getAllCountries(BaseSchema):
        
        pass 
        
    
    class getCountries(BaseSchema):
        
        
        onboarding = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
        
        phone_code = fields.Str(required=False)
         
        
    
    class getCountry(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
         
        
    
    class getDeliveryPromise(BaseSchema):
        
        
        x__location__detail = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        locality_value = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class validateAddress(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
        
        template_name = fields.Str(required=False)
         
        
    
    class getFulfillmentOptions(BaseSchema):
        
        
        x__application__data = fields.Str(required=False)
        
        product_slug = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
         
        
    
    class getFulfillmentOptionStores(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    


