

"""Inventory Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        
        
    
    
        
        
    

class InventoryValidator:
    
    
    class getJobConfigByIntegrationType(BaseSchema):
        
        
        integration_type = fields.Str(required=False)
        
        disable = fields.Boolean(required=False)
         
        
    
    class getJobCodesMetrics(BaseSchema):
        
        
        daily_job = fields.Boolean(required=False)
        
        job_code = fields.Str(required=False)
         
        
    
    class saveJobCodesMetrics(BaseSchema):
        
        pass 
        
    
    

