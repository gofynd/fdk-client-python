

"""DocumentEngine Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        



class DocumentEngineValidator:
    
    
    class generateBulkPackageLabel(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class generateBulkBoxLabel(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class generateBulkShipmentLabel(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class generateNoc(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getLabelStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class getNocStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class getPresignedURL(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getLabelPresignedURL(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class getNocPresignedURL(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class generatePOSReceipts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

