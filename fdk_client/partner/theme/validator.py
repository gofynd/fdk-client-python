

"""Theme Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        

class ThemeValidator:
    
    
    class getAllPages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class createPage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class updateMultiplePages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class getPage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class updatePage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class deletePage(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class getApplicationThemes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class getThemeById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class updateTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class deleteTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class getOrganizationThemes(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class getOrganizationThemeDetails(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class updateDraftTheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class submitOrganizationTheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class deleteOrganizationTheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getLatestVersionOfThemeBySlug(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        slug_name = fields.Str(required=False)
         
        
    
    class createNewThemeInOrganization(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class createExtensionSectionDraft(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class publishExtensionSections(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class applyExtensionPreview(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_section_id = fields.Str(required=False)
         
        
    
    class removeExtensionPreview(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_section_id = fields.Str(required=False)
         
        
    
    class getThemeRejectionReasons(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
        
    
    class getThemeVersions(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        theme_slug = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class createTheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    

