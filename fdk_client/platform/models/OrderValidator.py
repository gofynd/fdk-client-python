"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderValidator:
    
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
        
        exclude_locked_shipments = fields.Boolean(required=False)
         
    
    class getShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        ordering_company_id = fields.Str(required=False)
        
        request_by_ext = fields.Str(required=False)
         
    
    class getOrderShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class getLaneConfig(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        super_lane = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channel = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        bag_status = fields.Str(required=False)
         
    
    class getApplicationShipments(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
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
         
    
    class getMetricCount(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getAppOrderShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class getfilters(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
         
    
    class createShipmentReport(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getReportsShipmentListing(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class upsertJioCode(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getBulkInvoice(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class bulkActionProcessXlsxFile(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class bulkActionDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class createOrder(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class invalidateShipmentCache(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class reassignLocation(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updateShipmentLock(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getAnnouncements(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        date = fields.Str(required=False)
         
    
    class updateAddress(BaseSchema):
        
        shipment_id = fields.Str(required=False)
        
        name = fields.Str(required=False)
        
        address = fields.Str(required=False)
        
        address_type = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        phone = fields.Str(required=False)
        
        email = fields.Str(required=False)
        
        landmark = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class click2Call(BaseSchema):
        
        caller = fields.Str(required=False)
        
        receiver = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
        
        calling_to = fields.Str(required=False)
        
        caller_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class statusUpdateInternalV4(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class processManifest(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getRoleBasedActions(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getShipmentHistory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Int(required=False)
        
        bag_id = fields.Int(required=False)
         
    
    class sendSmsNinja(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class checkOrderStatus(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    