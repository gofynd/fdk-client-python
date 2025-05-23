

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
         
        
    
    class appbrowse(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class browsefiles(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
        
        search = fields.Str(required=False)
         
        
    
    

