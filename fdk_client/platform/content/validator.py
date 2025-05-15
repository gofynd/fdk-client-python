

"""Content Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        



class ContentValidator:
    
    
    class getCustomFieldTypes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getResources(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCustomFieldDefinitions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        resources = fields.Str(required=False)
        
        types = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        slugs = fields.Str(required=False)
        
        namespaces = fields.Str(required=False)
         
        
    
    class getCustomFieldDefinitionByResource(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        resource = fields.Str(required=False)
        
        types = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        slugs = fields.Str(required=False)
        
        namespaces = fields.Str(required=False)
         
        
    
    class createCustomFieldDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
         
        
    
    class getCustomFieldDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
        
        resource = fields.Str(required=False)
        
        namespace = fields.Str(required=False)
         
        
    
    class updateCustomFieldDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
        
        resource = fields.Str(required=False)
        
        namespace = fields.Str(required=False)
         
        
    
    class deleteCustomFieldDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
        
        resource = fields.Str(required=False)
        
        namespace = fields.Str(required=False)
         
        
    
    class getCustomFieldsByResourceSlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
        
        resource_slug = fields.Str(required=False)
         
        
    
    class updateCustomFieldByResourceSlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
        
        resource_slug = fields.Str(required=False)
         
        
    
    class deleteCustomFieldsByResourceSlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
        
        resource_slug = fields.Str(required=False)
        
        ids = fields.Str(required=False)
         
        
    
    class createCustomObjectDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCustomObjectDefinitions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class getCustomObjectDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class updateCustomObjectDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class deleteCustomObjectDefinitionBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getCustomObjectsBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        definition_slug = fields.Str(required=False)
         
        
    
    class createCustomObjectBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_slug = fields.Str(required=False)
         
        
    
    class getCustomObjectBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_slug = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class deleteCustomObjectBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_slug = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class updateCustomObjectBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_slug = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getJobs(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        action_type = fields.Str(required=False)
         
        
    
    class importCustomObjectEntriesBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class exportCustomObjectEntriesBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class sampleCustomObjectBulkEntryBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    

