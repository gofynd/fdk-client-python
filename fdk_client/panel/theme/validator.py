

"""Theme Panel Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PanelModel import BaseSchema



    
    
        
        
    
    
        
    
    
        

class ThemeValidator:
    
    
    class getMarketplaceThemes(BaseSchema):
        
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class getMarketplaceThemeBySlug(BaseSchema):
        
        
        slug_name = fields.Str(required=False)
         
        
    
    class getMarketplaceThemeVersions(BaseSchema):
        
        
        slug_name = fields.Str(required=False)
         
        
    
    


