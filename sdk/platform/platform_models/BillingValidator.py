"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

class BillingValidator:
    
    class createSubscriptionCharge(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
    
    class getSubscriptionCharge(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
    
    class cancelSubscriptionCharge(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscription_id = fields.Str(required=False)
         
    
    class getInvoices(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getInvoiceById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        invoice_id = fields.Str(required=False)
         
    
    class getCustomerDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class upsertCustomerDetail(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getSubscription(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getFeatureLimitConfig(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class activateSubscriptionPlan(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class cancelSubscriptionPlan(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    