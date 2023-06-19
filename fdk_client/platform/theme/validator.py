

"""Theme Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
        



class ThemeValidator:
    
    
    class getCompanyLevelThemes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class addMarketplaceThemeToCompany(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class deleteCompanyTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    

