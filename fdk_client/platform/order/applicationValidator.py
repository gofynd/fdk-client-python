

"""Order Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

class OrderValidator:
    
    
    class getApplicationOrderDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        previous = fields.Str(required=False)
         
        
    
    class trackShipmentPlatform(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class trackOrder(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
        
    
    class failedOrders(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class reprocessOrder(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
        
    
    class updateShipment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getPlatformShipmentReasons(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
        
    
    class getShipmentTrackDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getOrdersByApplicationId(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        filter_type = fields.Str(required=False)
         
        
    
    

