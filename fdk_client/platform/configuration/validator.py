

"""Configuration Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
        
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        



class ConfigurationValidator:
    
    
    class createApplication(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getApplications(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getCurrencies(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createCurrency(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCurrency(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateCurrency(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getDomainAvailibility(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getBrandsByCompany(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getCompanyByBrands(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getStoreByBrands(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getOtherSellerApplications(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getOtherSellerApplicationById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        app_id = fields.Str(required=False)
         
        
    
    class optOutFromApplication(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        app_id = fields.Str(required=False)
         
        
    
    class getLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        location_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getStoresForACompany(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        company = fields.Int(required=False)
         
        
    
    class getDomainOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

