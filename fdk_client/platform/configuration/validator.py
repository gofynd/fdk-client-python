

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
         
        
    
    class getIntegrationById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getAvailableOptIns(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getSelectedOptIns(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getIntegrationLevelConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        opted = fields.Boolean(required=False)
        
        check_permission = fields.Boolean(required=False)
         
        
    
    class updateLevelIntegration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
         
        
    
    class getIntegrationByLevelId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
        
    
    class updateLevelUidIntegration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
        
    
    class getLevelActiveIntegrations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
        
    
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
         
        
    
    

