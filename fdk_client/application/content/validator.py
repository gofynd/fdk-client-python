

"""Content Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
    
        
        
        
    
    
        
        
        
        
    
    
    
    
    
        
    
    
        
    
    
        
    
    
    
    
        
        
    
    
    
        
        
    
    
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    

class ContentValidator:
    
    
    class getAnnouncements(BaseSchema):
        
        pass 
        
    
    class getBlog(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
        
        preview = fields.Boolean(required=False)
         
        
    
    class getBlogs(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        tags = fields.Str(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class getDataLoaders(BaseSchema):
        
        pass 
        
    
    class getFaqs(BaseSchema):
        
        pass 
        
    
    class getFaqCategories(BaseSchema):
        
        pass 
        
    
    class getFaqBySlug(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class getFaqCategoryBySlug(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class getFaqsByCategorySlug(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class getLandingPage(BaseSchema):
        
        pass 
        
    
    class getLegalInformation(BaseSchema):
        
        pass 
        
    
    class getNavigations(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getSEOConfiguration(BaseSchema):
        
        pass 
        
    
    class getSEOMarkupSchemas(BaseSchema):
        
        
        page_type = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
         
        
    
    class getSupportInformation(BaseSchema):
        
        pass 
        
    
    class getTags(BaseSchema):
        
        pass 
        
    
    class getPage(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
        
    
    class getPages(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getCustomObjectBySlug(BaseSchema):
        
        
        definition_slug = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getCustomFieldsByResourceId(BaseSchema):
        
        
        resource = fields.Str(required=False)
        
        resource_slug = fields.Str(required=False)
         
        
    
    class getBulkCustomFieldsByResource(BaseSchema):
        
        
        resource = fields.Str(required=False)
        
        resource_ids = fields.Str(required=False)
        
        keys = fields.Str(required=False)
        
        namespaces = fields.Str(required=False)
         
        
    
    class getTranslateUILabels(BaseSchema):
        
        
        template = fields.Boolean(required=False)
        
        template_theme_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        locale = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class fetchResourceTranslations(BaseSchema):
        
        
        type = fields.Str(required=False)
        
        locale = fields.Str(required=False)
        
        resource_id = fields.Str(required=False)
         
        
    
    class fetchResourceTranslationsWithPayload(BaseSchema):
        
        
        type = fields.Str(required=False)
        
        locale = fields.Str(required=False)
         
        
    
    class getSupportedLanguages(BaseSchema):
        
        pass 
        
    
    class getOrderTranslation(BaseSchema):
        
        pass 
        
    
    


