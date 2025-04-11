

"""Theme Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
    
    
    
        

class ThemeValidator:
    
    
    class getAllPages(BaseSchema):
        
        
        theme_id = fields.Str(required=False)
         
        
    
    class getPage(BaseSchema):
        
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
        
        filters = fields.Str(required=False)
        
        section_preview_hash = fields.Str(required=False)
        
        company = fields.Int(required=False)
         
        
    
    class getAppliedTheme(BaseSchema):
        
        
        filters = fields.Boolean(required=False)
         
        
    
    class getThemeForPreview(BaseSchema):
        
        
        theme_id = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
         
        
    
    class getAppliedThemeV1(BaseSchema):
        
        pass 
        
    
    class getThemeForPreviewV1(BaseSchema):
        
        
        theme_id = fields.Str(required=False)
         
        
    
    


