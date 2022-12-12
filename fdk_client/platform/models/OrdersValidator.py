"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrdersValidator:
    
    class getShipments(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
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
        
        is_priority_sort = fields.Boolean(required=False)
        
        exclude_locked_shipments = fields.Boolean(required=False)
        
        payment_methods = fields.Str(required=False)
        
        channel_shipment_id = fields.Str(required=False)
        
        channel_order_id = fields.Str(required=False)
        
        custom_meta = fields.Str(required=False)
         
    
    class getShipmentById(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        channel_shipment_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        ordering_company_id = fields.Str(required=False)
        
        request_by_ext = fields.Str(required=False)
         
    
    class getOrderById(BaseSchema):
        
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
        
        custom_meta = fields.Str(required=False)
         
    
    class getMetricCount(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getAppOrderShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class trackPlatformShipment(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
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
        
        doc_type = fields.Str(required=False)
         
    
    class getBulkInvoiceLabel(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class getBulkShipmentExcelFile(BaseSchema):
        
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
         
    
    class getBulkList(BaseSchema):
        
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
         
    
    class getManifestList(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        status = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        search_value = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getManifestDetailsWithShipments(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        manifest_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        page = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        dp_ids = fields.Int(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
         
    
    class getBulkActionFailedReport(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
        
        report_type = fields.Str(required=False)
         
    
    class getShipmentReasons(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
        
        state = fields.Str(required=False)
         
    
    class bulkActionProcessXlsxFile(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class bulkActionDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class getBagById(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        bag_id = fields.Str(required=False)
        
        channel_bag_id = fields.Str(required=False)
        
        channel_id = fields.Str(required=False)
         
    
    class getBags(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        bag_ids = fields.Str(required=False)
        
        shipment_ids = fields.Str(required=False)
        
        order_ids = fields.Str(required=False)
        
        channel_bag_ids = fields.Str(required=False)
        
        channel_shipment_ids = fields.Str(required=False)
        
        channel_order_ids = fields.Str(required=False)
        
        channel_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    