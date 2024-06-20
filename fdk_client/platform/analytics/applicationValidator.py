

"""Analytics Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
    
    
        
        
        
    
    
        
        
        

class AnalyticsValidator:
    
    
    class executeJobForProvidedParametersV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class startDownloadForQueryV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
         
        
    
    class checkJobStatusByNameV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        file_name = fields.Str(required=False)
         
        
    
    

