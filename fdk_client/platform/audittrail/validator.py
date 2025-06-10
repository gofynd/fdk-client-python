

"""AuditTrail Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        



class AuditTrailValidator:
    
    
    class createAuditLog(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

