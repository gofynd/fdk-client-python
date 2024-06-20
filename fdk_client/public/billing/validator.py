

"""Billing Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        
    
    
        
    

class BillingValidator:
    
    
    class getStandardPlans(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class getPlanDetails(BaseSchema):
        
        
        plan_id = fields.Str(required=False)
         
        
    
    class planList(BaseSchema):
        
        pass 
        
    
    

