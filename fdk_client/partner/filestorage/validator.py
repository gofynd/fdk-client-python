

"""FileStorage Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
    
    
        

class FileStorageValidator:
    
    
    class getAllNamespaceDetails(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getNamespaceDetail(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class completeUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class startUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class browse(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
         
        
    
    class browseFiles(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
         
        
    
    class organizationLevelFetchProxy(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        url = fields.Str(required=False)
         
        
    
    class saveOrganizationLevelProxy(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class fetchProxy(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        url = fields.Str(required=False)
         
        
    
    class saveProxyDetails(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class signUrls(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    

