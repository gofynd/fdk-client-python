

"""Billing Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        



class BillingValidator:
    
    
    class getChargeDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        charge_id = fields.Str(required=False)
         
        
    
    class getSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
        
    
    class cancelSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
        
    
    class createOneTimeCharge(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class createSubscriptionCharge(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    

