

"""FileStorage Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
        
    

class FileStorageValidator:
    
    
    class startUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
         
        
    
    class completeUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
         
        
    
    class signUrls(BaseSchema):
        
        pass 
        
    
    


