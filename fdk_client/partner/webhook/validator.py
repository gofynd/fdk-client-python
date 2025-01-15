

"""Webhook Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        

class WebhookValidator:
    
    
    class responseTimeSummary(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class fetchDeliverySummary(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class getDeliveryDetailInsights(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class fetchDeliveryTs(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class fetchReportFilters(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class cancelReportDownload(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        filename = fields.Str(required=False)
         
        
    
    class getHistoricalReports(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class getInvalidEventList(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class fetchSubscribers(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class updateSubscriber(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        subscriber_id = fields.Float(required=False)
         
        
    
    

