

"""Analytics Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        



class AnalyticsValidator:
    
    
    class createExportJob(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
         
        
    
    class getExportJobStatus(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
        
    
    class getLogsList(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        log_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class searchLogs(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        log_type = fields.Str(required=False)
         
        
    
    

