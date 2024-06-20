

"""FileStorage Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        

class FileStorageValidator:
    
    
    class startUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class completeUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
         
        
    
    class browse(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        organization_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
         
        
    
    

