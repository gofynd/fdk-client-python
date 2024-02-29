

"""Billing Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        

class BillingValidator:
    
    
    class getStandardPlans(BaseSchema):
        
        
        platform_type = fields.Str(required=False)
         
        
    
    

