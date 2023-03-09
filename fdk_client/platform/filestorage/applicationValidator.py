

"""FileStorage Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        

class FileStorageValidator:
    
    
    class appStartUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class appCompleteUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class appCopyFiles(BaseSchema):
        
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
         
        
    
    class browse(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    

