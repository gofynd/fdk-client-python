

"""Order Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
    
    
        
        
        
        
        
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
        
        
    
    
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
    
    
        
        



class OrderValidator:
    
    
    class reassignLocation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class updateShipmentLock(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getAnnouncements(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        date = fields.Str(required=False)
         
        
    
    class updateAddress(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class updateShipmentStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getRoleBasedActions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getShipmentHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        bag_id = fields.Int(required=False)
         
        
    
    class postShipmentHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class sendSmsNinja(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class updatePackagingDimensions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getChannelConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createChannelConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class orderUpdate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class checkOrderStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getStateTransitionMap(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getAllowedStateTransition(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        ordering_channel = fields.Str(required=False)
        
        ordering_source = fields.Str(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class fetchRefundModeConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class attachOrderUser(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class sendUserMobileOTP(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class verifyMobileOTP(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class downloadLanesReport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class bulkStateTransistion(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class bulkListing(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        bulk_action_type = fields.Str(required=False)
        
        search_key = fields.Str(required=False)
         
        
    
    class jobDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class getFileByStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        file_type = fields.Str(required=False)
        
        report_type = fields.Str(required=False)
         
        
    
    class getManifestShipments(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Int(required=False)
        
        to_date = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        dp_name = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getManifests(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        status = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        search_value = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class generateProcessManifest(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getManifestDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        manifest_id = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class dispatchManifests(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class uploadConsents(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getManifestfilters(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
         
        
    
    class eInvoiceRetry(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class trackShipment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        awb = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class updateShipmentTracking(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class failedOrderLogs(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
         
        
    
    class generateInvoiceID(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        invoice_type = fields.Str(required=False)
         
        
    
    class failedOrderLogDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        log_id = fields.Str(required=False)
         
        
    
    class addStateManagerConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getStateManagerConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        app_id = fields.Str(required=False)
        
        ordering_channel = fields.Str(required=False)
        
        ordering_source = fields.Str(required=False)
        
        entity = fields.Str(required=False)
         
        
    
    class updatePaymentInfo(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class createOrder(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        x__ordering__source = fields.Str(required=False)
        
        x__application__id = fields.Str(required=False)
        
        x__extension__id = fields.Str(required=False)
         
        
    
    class createAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class listAccounts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page = fields.Int(required=False)
        
        size = fields.Int(required=False)
         
        
    
    class getAccountById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        channel_account_id = fields.Str(required=False)
         
        
    
    class updateAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        channel_account_id = fields.Str(required=False)
         
        
    
    class getShipmentPackages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class createShipmentPackages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class updateShipmentPackages(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getShipments(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        bag_status = fields.Str(required=False)
        
        status_assigned = fields.Str(required=False)
        
        status_override_lane = fields.Boolean(required=False)
        
        time_to_dispatch = fields.Int(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        status_assigned_start_date = fields.Str(required=False)
        
        status_assigned_end_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        fetch_active_shipment = fields.Boolean(required=False)
        
        allow_inactive = fields.Boolean(required=False)
        
        exclude_locked_shipments = fields.Boolean(required=False)
        
        payment_methods = fields.Str(required=False)
        
        channel_shipment_id = fields.Str(required=False)
        
        channel_order_id = fields.Str(required=False)
        
        custom_meta = fields.Str(required=False)
        
        ordering_channel = fields.Str(required=False)
        
        company_affiliate_tag = fields.Str(required=False)
        
        my_orders = fields.Boolean(required=False)
        
        platform_user_id = fields.Str(required=False)
        
        sort_type = fields.Str(required=False)
        
        show_cross_company_data = fields.Boolean(required=False)
        
        tags = fields.Str(required=False)
        
        customer_id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
        
        enforce_date_filter = fields.Boolean(required=False)
        
        fulfillment_type = fields.Str(required=False)
        
        ordering_source = fields.Str(required=False)
        
        channel_account_id = fields.Str(required=False)
         
        
    
    class getShipmentById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        channel_shipment_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        fetch_active_shipment = fields.Boolean(required=False)
        
        allow_inactive = fields.Boolean(required=False)
         
        
    
    class getOrderById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        order_id = fields.Str(required=False)
        
        my_orders = fields.Boolean(required=False)
        
        allow_inactive = fields.Boolean(required=False)
         
        
    
    class getLaneConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        super_lane = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        bag_status = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        time_to_dispatch = fields.Int(required=False)
        
        payment_methods = fields.Str(required=False)
        
        my_orders = fields.Boolean(required=False)
        
        show_cross_company_data = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class getOrders(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        lane = fields.Str(required=False)
        
        search_type = fields.Str(required=False)
        
        bag_status = fields.Str(required=False)
        
        time_to_dispatch = fields.Int(required=False)
        
        payment_methods = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        search_value = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_priority_sort = fields.Boolean(required=False)
        
        custom_meta = fields.Str(required=False)
        
        my_orders = fields.Boolean(required=False)
        
        show_cross_company_data = fields.Boolean(required=False)
        
        customer_id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        allow_inactive = fields.Boolean(required=False)
        
        group_entity = fields.Str(required=False)
        
        enforce_date_filter = fields.Boolean(required=False)
        
        fulfillment_type = fields.Str(required=False)
        
        ordering_source = fields.Str(required=False)
        
        channel_account_id = fields.Str(required=False)
         
        
    
    class getfilters(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
        
        group_entity = fields.Str(required=False)
         
        
    
    class getBulkShipmentExcelFile(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        sales_channels = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        bag_status = fields.Str(required=False)
        
        payment_methods = fields.Str(required=False)
        
        file_type = fields.Str(required=False)
        
        time_to_dispatch = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getBulkActionTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class downloadBulkActionTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        template_slug = fields.Str(required=False)
         
        
    
    class getShipmentReasons(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
        
        state = fields.Str(required=False)
         
        
    
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
         
        
    
    class generatePOSReceiptByOrderId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        document_type = fields.Str(required=False)
         
        
    
    class getAllowedTemplatesForBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        template_name = fields.Str(required=False)
         
        
    
    

