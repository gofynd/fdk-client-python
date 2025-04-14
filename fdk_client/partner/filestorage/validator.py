

"""FileStorage Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
    
    
        

class FileStorageValidator:
    
    
    class completeUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class startUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class browseFiles(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
         
        
    
    class fetchProxy(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        url = fields.Str(required=False)
         
        
    
    class saveProxyDetails(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class signUrls(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    

