

"""Order Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
    
    
        
        
        

class OrderValidator:
    
    
    class trackShipmentPlatform(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getPlatformShipmentReasons(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
        
    
    

