"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrdersValidator:
    
    class getShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        ordering_company_id = fields.Str(required=False)
        
        request_by_ext = fields.Str(required=False)
         
    
    class getLaneConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        super_lane = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getOrderShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class getShipmentList(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        search_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        ordering_company_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channel = fields.Str(required=False)
        
        request_by_ext = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        customer_id = fields.Str(required=False)
        
        is_priority_sort = fields.Boolean(required=False)
         
    
    class getShipmentToManifest(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        group_entity = fields.Str(required=False)
        
        sales_channel = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
         
    
    class getOrders(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channel = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_priority_sort = fields.Boolean(required=False)
         
    
    class getfilters(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
         
    