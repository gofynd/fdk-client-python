

"""Logistic Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    

class LogisticValidator:
    
    
    class getPincodeCity(BaseSchema):
        
        
        pincode = fields.Str(required=False)
         
        
    
    class getAllCountries(BaseSchema):
        
        pass 
        
    
    class getZones(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        sector = fields.Str(required=False)
        
        store_uid = fields.Int(required=False)
        
        region_uid = fields.Str(required=False)
         
        
    
    class getGeoAreas(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        type = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        onboard = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
         
        
    
    class getCountry(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
         
        
    
    class getLocalitiesByPrefix(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        name = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        locality_type = fields.Str(required=False)
        
        locality_value = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
         
        
    
    class validateAddress(BaseSchema):
        
        
        country_iso_code = fields.Str(required=False)
        
        template_name = fields.Str(required=False)
         
        
    
    class createShipments(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getDeliveryPromise(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getQCPromise(BaseSchema):
        
        pass 
        
    
    


