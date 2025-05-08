

"""Theme Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        

class ThemeValidator:
    
    
    class getAllPages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class createPage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class updateMultiplePages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getPage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
        
    
    class deletePage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
        
    
    class updatePage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
        
        socket_id = fields.Str(required=False)
         
        
    
    class getFonts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getApplicationThemes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getApplicationThemesCount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getThemeById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class updateTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class deleteTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class addThemeToApplication(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateThemeName(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class applyTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class duplicateTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getAppliedTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getThemeForPreview(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getThemeLastModified(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class isUpgradable(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class upgradeTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getExtensionSections(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        company_mode = fields.Str(required=False)
         
        
    
    

