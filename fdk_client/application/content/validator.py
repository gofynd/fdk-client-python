

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
        
    
    class getPages(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getPage(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
        
    
    class getCustomObject(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class getCustomObjects(BaseSchema):
        
        
        definition_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        ids = fields.Str(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class getCustomFieldDefinitions(BaseSchema):
        
        pass 
        
    
    class getCustomFieldDefinition(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class getCustomFields(BaseSchema):
        
        
        resource = fields.Str(required=False)
        
        resource_ids = fields.Str(required=False)
         
        
    
    


