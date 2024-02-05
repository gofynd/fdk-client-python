

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
         
        
    
    class createCustomFieldDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCustomFieldDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class updateCustomFieldDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class deleteCustomFieldDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class getCustomFields(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
         
        
    
    class getCustomFieldsByResourceId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
        
        resource_id = fields.Str(required=False)
         
        
    
    class createCustomFieldByResourceId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        resource = fields.Str(required=False)
        
        resource_id = fields.Str(required=False)
         
        
    
    class createCustomObjectDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCustomObjectDefinitions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class getCustomObjectDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class updateCustomObjectDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class deleteCustomObjectDefinition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class getCustomObjects(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
         
        
    
    class createCustomObject(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCustomObject(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        metaobject_id = fields.Str(required=False)
         
        
    
    class deleteCustomObject(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        metaobject_id = fields.Str(required=False)
         
        
    
    class updateCustomObject(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        metaobject_id = fields.Str(required=False)
         
        
    
    class getJobs(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        action_type = fields.Str(required=False)
         
        
    
    class importCustomObjectEntries(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class exportCustomObjectEntries(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    class sampleCustomObjectBulkEntry(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        definition_id = fields.Str(required=False)
         
        
    
    

