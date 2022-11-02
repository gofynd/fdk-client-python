

"""Order Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
        
    
    
        
    
    
        
        
    
    
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        



class OrderValidator:
    
    
    class shipmentStatusUpdate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class activityStatus(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
         
        
    
    class storeProcessShipmentUpdate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class checkRefund(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class shipmentBagsCanBreak(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getOrdersByCompanyId(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        is_priority_sort = fields.Boolean(required=False)
        
        lock_status = fields.Boolean(required=False)
        
        user_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        deployment_stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        filter_type = fields.Str(required=False)
         
        
    
    class getOrderLanesCountByCompanyId(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
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
        
        filter_type = fields.Str(required=False)
         
        
    
    class getOrderDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        previous = fields.Str(required=False)
         
        
    
    class getPicklistOrdersByCompanyId(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
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
        
        filter_type = fields.Str(required=False)
         
        
    
    class getShipmentAddress(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
        
    
    class updateShipmentAddress(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
        
    
    
