

"""Webhook Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
        
        



class WebhookValidator:
    
    
    class manualRetryOfFailedEvent(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getEventCounts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getManualRetryStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class manualRetryCancel(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class downloadDeliveryReport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class pingWebhook(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getReportFilters(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getHistoricalReports(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class cancelJobByName(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        filename = fields.Str(required=False)
         
        
    
    class getDeliveryReports(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class fetchAllEventConfigurations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class registerSubscriberToEventV2(BaseSchema):
        
        
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
         
        
    
    class getSubscriberById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        subscriber_id = fields.Int(required=False)
         
        
    
    class getSubscribersByExtensionId(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    

