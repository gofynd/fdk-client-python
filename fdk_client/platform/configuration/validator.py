

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
        
        id = fields.Str(required=False)
         
        
    
    class optOutFromApplication(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getCurrencyExchangeRates(BaseSchema):
        
        
        currency_code = fields.Str(required=False)
        
        exchange_currency_code = fields.Str(required=False)
        
        exchange_country_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    

