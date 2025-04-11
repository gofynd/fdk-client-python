

"""Webhook Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
        
        



class WebhookValidator:
    
    
    class fetchAllEventConfigurations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class registerSubscriberToEventV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class updateSubscriberV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class registerSubscriberToEvent(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getSubscribersByCompany(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class updateSubscriberConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class upsertSubscriberEvent(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getSubscriberById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        subscriber_id = fields.Int(required=False)
         
        
    
    class getSubscribersByExtensionId(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    

