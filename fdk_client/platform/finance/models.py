"""Finance Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class GenerateReportMeta(BaseSchema):
    pass


class GenerateReportFilters(BaseSchema):
    pass


class GenerateReportPlatform(BaseSchema):
    pass


class GenerateReportRequest(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class GenerateReportJson(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class DownloadReport(BaseSchema):
    pass


class DownloadReportItems(BaseSchema):
    pass


class DownloadReportList(BaseSchema):
    pass


class GetEngineData(BaseSchema):
    pass


class GetEngineRequest(BaseSchema):
    pass


class GetEngineResponse(BaseSchema):
    pass


class GetReason(BaseSchema):
    pass


class GetReasonRequest(BaseSchema):
    pass


class ReasonItem(BaseSchema):
    pass


class GetReasonResponse(BaseSchema):
    pass


class GetReportListData(BaseSchema):
    pass


class GetReportListRequest(BaseSchema):
    pass


class GetAffiliate(BaseSchema):
    pass


class GetReportListResponse(BaseSchema):
    pass


class ReportItem(BaseSchema):
    pass


class GetAffiliateResponse(BaseSchema):
    pass


class DownloadCreditDebitNote(BaseSchema):
    pass


class DownloadCreditDebitNoteRequest(BaseSchema):
    pass


class DownloadCreditDebitNoteResponseData(BaseSchema):
    pass


class DownloadCreditDebitNoteResponse(BaseSchema):
    pass


class PaymentProcessPayload(BaseSchema):
    pass


class PaymentProcessRequest(BaseSchema):
    pass


class PaymentProcessResponse(BaseSchema):
    pass


class CreditlineDataPlatformPayload(BaseSchema):
    pass


class CreditlineDataPlatformRequest(BaseSchema):
    pass


class CreditlineDataPlatformResponse(BaseSchema):
    pass


class IsCreditlinePayload(BaseSchema):
    pass


class IsCreditlinePlatformRequest(BaseSchema):
    pass


class IsCreditlinePlatformResponse(BaseSchema):
    pass


class InvoiceTypePayloadData(BaseSchema):
    pass


class InvoiceTypeRequest(BaseSchema):
    pass


class InvoiceTypeResponseItems(BaseSchema):
    pass


class InvoiceTypeResponse(BaseSchema):
    pass


class InoviceListingPayloadDataFilters(BaseSchema):
    pass


class InvoiceListingPayloadData(BaseSchema):
    pass


class InvoiceListingRequest(BaseSchema):
    pass


class UnpaidInvoiceDataItems(BaseSchema):
    pass


class InvoiceListingResponseItems(BaseSchema):
    pass


class InvoiceListingResponse(BaseSchema):
    pass


class InvoicePdfPayloadData(BaseSchema):
    pass


class InvoicePdfRequest(BaseSchema):
    pass


class InvoicePdfResponse(BaseSchema):
    pass


class IsCnRefundMethodData(BaseSchema):
    pass


class IsCnRefundMethodRequest(BaseSchema):
    pass


class IsCnRefundMethodResponseData(BaseSchema):
    pass


class IsCnRefundMethodResponse(BaseSchema):
    pass


class CreditNoteConfigNotificationEvents(BaseSchema):
    pass


class CreateSellerCreditNoteConfig(BaseSchema):
    pass


class CreateSellerCreditNoteConfigRequest(BaseSchema):
    pass


class CreateSellerCreditNoteConfigResponse(BaseSchema):
    pass


class DeleteConfig(BaseSchema):
    pass


class DeleteConfigRequest(BaseSchema):
    pass


class DeleteConfigResponse(BaseSchema):
    pass


class ChannelDisplayName(BaseSchema):
    pass


class ChannelDisplayNameResponse(BaseSchema):
    pass


class CnReferenceNumber(BaseSchema):
    pass


class GetPdfUrlViewRequest(BaseSchema):
    pass


class GetPdfUrlViewResponseData(BaseSchema):
    pass


class GetPdfUrlViewResponse(BaseSchema):
    pass


class CreditNoteDetailsRequest(BaseSchema):
    pass


class CnDetails(BaseSchema):
    pass


class RedemptionDetails(BaseSchema):
    pass


class CreditNoteDetails(BaseSchema):
    pass


class CreditNoteDetailsResponse(BaseSchema):
    pass


class GetCustomerCreditBalance(BaseSchema):
    pass


class GetCustomerCreditBalanceRequest(BaseSchema):
    pass


class GetCustomerCreditBalanceResponseData(BaseSchema):
    pass


class GetCustomerCreditBalanceResponse(BaseSchema):
    pass


class GetCnConfigRequest(BaseSchema):
    pass


class GetCnConfigResponseMeta(BaseSchema):
    pass


class GetCnConfigResponseData(BaseSchema):
    pass


class GetCnConfigResponse(BaseSchema):
    pass


class CnGenerateReportFilters(BaseSchema):
    pass


class CnGenerateReport(BaseSchema):
    pass


class GenerateReportCustomerCnRequest(BaseSchema):
    pass


class CnGenerateReportItems(BaseSchema):
    pass


class GenerateReportCustomerCnResponseData(BaseSchema):
    pass


class GenerateReportCustomerCnResponse(BaseSchema):
    pass


class CnDownloadReport(BaseSchema):
    pass


class DownloadReportCustomerCnRequest(BaseSchema):
    pass


class DownloadReportResponseData(BaseSchema):
    pass


class DownloadReportCustomerCnResponse(BaseSchema):
    pass


class GetReportingFilters(BaseSchema):
    pass


class GetReportingNestedFilters(BaseSchema):
    pass


class GetReportingFiltersResponse(BaseSchema):
    pass





class GenerateReportMeta(BaseSchema):
    # Finance swagger.json

    
    brand = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    


class GenerateReportFilters(BaseSchema):
    # Finance swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    company = fields.List(fields.Str(required=False), required=False)
    
    channel = fields.List(fields.Str(required=False), required=False)
    


class GenerateReportPlatform(BaseSchema):
    # Finance swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    


class GenerateReportRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GenerateReportPlatform, required=False)
    


class Page(BaseSchema):
    # Finance swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class GenerateReportJson(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    end_date = fields.Str(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    item_count = fields.Int(required=False)
    


class Error(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class DownloadReport(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    pagesize = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class DownloadReportItems(BaseSchema):
    # Finance swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    type_of_request = fields.Str(required=False)
    


class DownloadReportList(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Nested(DownloadReportItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    table_name = fields.Str(required=False)
    
    project = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Dict(required=False)
    


class GetEngineRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetEngineData, required=False)
    


class GetEngineResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    


class GetReason(BaseSchema):
    # Finance swagger.json

    
    reason_type = fields.Str(required=False)
    


class GetReasonRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReason, required=False)
    


class ReasonItem(BaseSchema):
    # Finance swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class GetReasonResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    item_list = fields.List(fields.Nested(ReasonItem, required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetReportListData(BaseSchema):
    # Finance swagger.json

    
    role_name = fields.Str(required=False)
    
    listing_enabled = fields.Boolean(required=False)
    


class GetReportListRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReportListData, required=False)
    


class GetAffiliate(BaseSchema):
    # Finance swagger.json

    
    company_id = fields.Int(required=False)
    


class GetReportListResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(ReportItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    total_count = fields.Int(required=False)
    


class ReportItem(BaseSchema):
    # Finance swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    allowed_filters = fields.List(fields.Str(required=False), required=False)
    
    config_meta = fields.Dict(required=False)
    
    report_type = fields.Str(required=False)
    
    display_date = fields.Str(required=False)
    


class GetAffiliateResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    docs = fields.List(fields.Dict(required=False), required=False)
    


class DownloadCreditDebitNote(BaseSchema):
    # Finance swagger.json

    
    note_id = fields.List(fields.Str(required=False), required=False)
    


class DownloadCreditDebitNoteRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DownloadCreditDebitNote, required=False)
    


class DownloadCreditDebitNoteResponseData(BaseSchema):
    # Finance swagger.json

    
    id = fields.Str(required=False)
    
    pdf_s3_url = fields.Str(required=False)
    


class DownloadCreditDebitNoteResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(DownloadCreditDebitNoteResponseData, required=False), required=False)
    


class PaymentProcessPayload(BaseSchema):
    # Finance swagger.json

    
    platform = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    transaction_type = fields.Str(required=False)
    
    source_reference = fields.Str(required=False)
    
    total_amount = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    seller_id = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    


class PaymentProcessRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(PaymentProcessPayload, required=False)
    


class PaymentProcessResponse(BaseSchema):
    # Finance swagger.json

    
    code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    transaction_id = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    


class CreditlineDataPlatformPayload(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    seller_id = fields.Str(required=False)
    
    end_end = fields.Str(required=False)
    
    start_end = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    


class CreditlineDataPlatformRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CreditlineDataPlatformPayload, required=False)
    


class CreditlineDataPlatformResponse(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    code = fields.Int(required=False)
    
    show_mr = fields.Boolean(required=False)
    
    page = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    item_count = fields.Int(required=False)
    


class IsCreditlinePayload(BaseSchema):
    # Finance swagger.json

    
    seller_id = fields.Str(required=False)
    


class IsCreditlinePlatformRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(IsCreditlinePayload, required=False)
    


class IsCreditlinePlatformResponse(BaseSchema):
    # Finance swagger.json

    
    is_creditline_opted = fields.Boolean(required=False)
    
    code = fields.Int(required=False)
    


class InvoiceTypePayloadData(BaseSchema):
    # Finance swagger.json

    
    is_active = fields.Boolean(required=False)
    


class InvoiceTypeRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoiceTypePayloadData, required=False)
    


class InvoiceTypeResponseItems(BaseSchema):
    # Finance swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class InvoiceTypeResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    invoice_type_list = fields.List(fields.Nested(InvoiceTypeResponseItems, required=False), required=False)
    
    payment_status_list = fields.List(fields.Nested(InvoiceTypeResponseItems, required=False), required=False)
    


class InoviceListingPayloadDataFilters(BaseSchema):
    # Finance swagger.json

    
    payment_status = fields.List(fields.Str(required=False), required=False)
    
    invoice_type = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.List(fields.Str(required=False), required=False)
    


class InvoiceListingPayloadData(BaseSchema):
    # Finance swagger.json

    
    page_size = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    search = fields.Str(required=False)
    
    filters = fields.Nested(InoviceListingPayloadDataFilters, required=False)
    


class InvoiceListingRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoiceListingPayloadData, required=False)
    


class UnpaidInvoiceDataItems(BaseSchema):
    # Finance swagger.json

    
    total_unpaid_invoice_count = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    total_unpaid_amount = fields.Float(required=False)
    


class InvoiceListingResponseItems(BaseSchema):
    # Finance swagger.json

    
    amount = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    
    period = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    
    is_downloadable = fields.Boolean(required=False)
    
    invoice_id = fields.Str(required=False)
    


class InvoiceListingResponse(BaseSchema):
    # Finance swagger.json

    
    unpaid_invoice_data = fields.Nested(UnpaidInvoiceDataItems, required=False)
    
    items = fields.List(fields.Nested(InvoiceListingResponseItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    


class InvoicePdfPayloadData(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.List(fields.Str(required=False), required=False)
    


class InvoicePdfRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoicePdfPayloadData, required=False)
    


class InvoicePdfResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Str(required=False), required=False)
    
    error = fields.List(fields.Str(required=False), required=False)
    


class IsCnRefundMethodData(BaseSchema):
    # Finance swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    toggle_edit_required = fields.Boolean(required=False)
    
    seller_id = fields.Int(required=False)
    


class IsCnRefundMethodRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(IsCnRefundMethodData, required=False)
    


class IsCnRefundMethodResponseData(BaseSchema):
    # Finance swagger.json

    
    is_first_time_user = fields.Boolean(required=False)
    


class IsCnRefundMethodResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(IsCnRefundMethodResponseData, required=False)
    


class CreditNoteConfigNotificationEvents(BaseSchema):
    # Finance swagger.json

    
    expiration_reminder_to_customer = fields.Int(required=False)
    


class CreateSellerCreditNoteConfig(BaseSchema):
    # Finance swagger.json

    
    is_cn_as_refund_method = fields.Boolean(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    source_channel = fields.List(fields.Str(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    
    notification_events = fields.Nested(CreditNoteConfigNotificationEvents, required=False)
    
    sales_channel_name = fields.Str(required=False)
    
    ordering_channel = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Int(required=False)
    
    currency_type = fields.Str(required=False)
    
    slug_values = fields.List(fields.Str(required=False), required=False)
    


class CreateSellerCreditNoteConfigRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CreateSellerCreditNoteConfig, required=False)
    


class CreateSellerCreditNoteConfigResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class DeleteConfig(BaseSchema):
    # Finance swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    slug_values = fields.List(fields.Str(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    


class DeleteConfigRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DeleteConfig, required=False)
    


class DeleteConfigResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ChannelDisplayName(BaseSchema):
    # Finance swagger.json

    
    platform_pos = fields.Str(required=False)
    


class ChannelDisplayNameResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ChannelDisplayName, required=False)
    


class CnReferenceNumber(BaseSchema):
    # Finance swagger.json

    
    cn_reference_number = fields.Str(required=False)
    


class GetPdfUrlViewRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CnReferenceNumber, required=False)
    


class GetPdfUrlViewResponseData(BaseSchema):
    # Finance swagger.json

    
    s3_pdf_link = fields.Str(required=False)
    
    cn_reference_number = fields.Str(required=False)
    


class GetPdfUrlViewResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(GetPdfUrlViewResponseData, required=False)
    


class CreditNoteDetailsRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CnReferenceNumber, required=False)
    


class CnDetails(BaseSchema):
    # Finance swagger.json

    
    staff_id = fields.Str(required=False)
    
    expiry_date = fields.Str(required=False)
    
    channel_of_issuance = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    date_issued = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    store_id = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    


class RedemptionDetails(BaseSchema):
    # Finance swagger.json

    
    staff_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    store_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    amount_debited = fields.Int(required=False)
    
    invoice_number = fields.Str(required=False)
    


class CreditNoteDetails(BaseSchema):
    # Finance swagger.json

    
    cn_status = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    
    cn_reference_number = fields.Str(required=False)
    
    cn_details = fields.Dict(required=False)
    
    redemption_details = fields.List(fields.Nested(RedemptionDetails, required=False), required=False)
    
    remaining_cn_amount = fields.Int(required=False)
    
    available_cn_balance = fields.Int(required=False)
    
    cn_amount = fields.Int(required=False)
    


class CreditNoteDetailsResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreditNoteDetails, required=False)
    


class GetCustomerCreditBalance(BaseSchema):
    # Finance swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    


class GetCustomerCreditBalanceRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetCustomerCreditBalance, required=False)
    


class GetCustomerCreditBalanceResponseData(BaseSchema):
    # Finance swagger.json

    
    customer_mobile_number = fields.Str(required=False)
    
    total_credited_balance = fields.Int(required=False)
    


class GetCustomerCreditBalanceResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(GetCustomerCreditBalanceResponseData, required=False)
    


class GetCnConfigRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DeleteConfig, required=False)
    


class GetCnConfigResponseMeta(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    source_channel = fields.List(fields.Str(required=False), required=False)
    


class GetCnConfigResponseData(BaseSchema):
    # Finance swagger.json

    
    is_cn_as_refund_method = fields.Boolean(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    meta = fields.Nested(GetCnConfigResponseMeta, required=False)
    
    seller_id = fields.Int(required=False)
    
    notification_events = fields.Nested(CreditNoteConfigNotificationEvents, required=False)
    
    validity = fields.Int(required=False)
    
    redemption_ordering_channel = fields.List(fields.Str(required=False), required=False)
    
    currency_type = fields.Str(required=False)
    


class GetCnConfigResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(GetCnConfigResponseData, required=False)
    


class CnGenerateReportFilters(BaseSchema):
    # Finance swagger.json

    
    staff_id = fields.List(fields.Str(required=False), required=False)
    
    channel_of_issuance = fields.List(fields.Str(required=False), required=False)
    
    utilisation = fields.List(fields.Str(required=False), required=False)
    
    ordering_channel = fields.List(fields.Str(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    types_of_transaction = fields.List(fields.Str(required=False), required=False)
    


class CnGenerateReport(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    
    filters = fields.Nested(CnGenerateReportFilters, required=False)
    
    affiliate_id = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportFilters, required=False)
    
    search = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    search_type = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    


class GenerateReportCustomerCnRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CnGenerateReport, required=False)
    


class CnGenerateReportItems(BaseSchema):
    # Finance swagger.json

    
    expiry_date = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    total_amount = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    date_issued = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    
    credit_note_number = fields.Str(required=False)
    


class GenerateReportCustomerCnResponseData(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Nested(CnGenerateReportItems, required=False), required=False)
    
    row_header_display_order = fields.Dict(required=False)
    
    end_date = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    primary_headers = fields.List(fields.Str(required=False), required=False)
    
    allowed_filters = fields.List(fields.Str(required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    item_count = fields.Int(required=False)
    


class GenerateReportCustomerCnResponse(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GenerateReportCustomerCnResponseData, required=False)
    


class CnDownloadReport(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    search = fields.Str(required=False)
    
    status = fields.List(fields.Str(required=False), required=False)
    
    search_type = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    


class DownloadReportCustomerCnRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CnDownloadReport, required=False)
    


class DownloadReportResponseData(BaseSchema):
    # Finance swagger.json

    
    report_config_id = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    requested_by = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    request_dict = fields.Dict(required=False)
    
    download_link = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    msg = fields.Str(required=False)
    
    report_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    filters = fields.Dict(required=False)
    


class DownloadReportCustomerCnResponse(BaseSchema):
    # Finance swagger.json

    
    data = fields.List(fields.Nested(DownloadReportResponseData, required=False), required=False)
    


class GetReportingFilters(BaseSchema):
    # Finance swagger.json

    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    options = fields.List(fields.Dict(required=False), required=False)
    
    value = fields.Str(required=False)
    


class GetReportingNestedFilters(BaseSchema):
    # Finance swagger.json

    
    text = fields.Str(required=False)
    
    options = fields.List(fields.Dict(required=False), required=False)
    
    required = fields.Boolean(required=False)
    
    placeholder_text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class GetReportingFiltersResponse(BaseSchema):
    # Finance swagger.json

    
    search = fields.Nested(GetReportingFilters, required=False)
    
    filters = fields.List(fields.Nested(GetReportingNestedFilters, required=False), required=False)
    
    status = fields.Nested(GetReportingFilters, required=False)
    


