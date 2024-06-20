"""Finance Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class OrederFreezeResponse(BaseSchema):
    pass


class GenerateReportMeta(BaseSchema):
    pass


class GenerateReportFilters(BaseSchema):
    pass


class GenerateReportPlatform(BaseSchema):
    pass


class GenerateReportReq(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class Currency(BaseSchema):
    pass


class GenerateReportJson(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class ErrorMeta(BaseSchema):
    pass


class ErrorMetaItems(BaseSchema):
    pass


class DownloadReport(BaseSchema):
    pass


class DownloadReportData(BaseSchema):
    pass


class DownloadReportItems(BaseSchema):
    pass


class DownloadReportList(BaseSchema):
    pass


class GetEngineFilters(BaseSchema):
    pass


class GetEngineData(BaseSchema):
    pass


class GetEngineReq(BaseSchema):
    pass


class GetEngineResponse(BaseSchema):
    pass


class GetReason(BaseSchema):
    pass


class GetReasonReq(BaseSchema):
    pass


class ReasonItem(BaseSchema):
    pass


class GetReasonResponse(BaseSchema):
    pass


class GetReportListData(BaseSchema):
    pass


class GetReportListReq(BaseSchema):
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


class DownloadCreditDebitNoteReq(BaseSchema):
    pass


class DownloadCreditDebitNoteResponseData(BaseSchema):
    pass


class DownloadCreditDebitNoteResponse(BaseSchema):
    pass


class PaymentProcessPayload(BaseSchema):
    pass


class PaymentProcessReq(BaseSchema):
    pass


class PaymentProcessResponse(BaseSchema):
    pass


class CreditlineDataPlatformPayload(BaseSchema):
    pass


class CreditlineDataPlatformReq(BaseSchema):
    pass


class CreditlineDataPlatformResponse(BaseSchema):
    pass


class IsCreditlinePayload(BaseSchema):
    pass


class IsCreditlinePlatformReq(BaseSchema):
    pass


class IsCreditlinePlatformResponse(BaseSchema):
    pass


class InvoiceTypePayloadData(BaseSchema):
    pass


class InvoiceTypeReq(BaseSchema):
    pass


class InvoiceTypeResponseItems(BaseSchema):
    pass


class InvoiceTypeResponse(BaseSchema):
    pass


class InoviceListingPayloadDataFilters(BaseSchema):
    pass


class InvoiceListingPayloadData(BaseSchema):
    pass


class InvoiceListingReq(BaseSchema):
    pass


class UnpaidInvoiceDataItems(BaseSchema):
    pass


class InvoiceListingResponseItems(BaseSchema):
    pass


class InvoiceListingResponse(BaseSchema):
    pass


class InvoicePdfPayloadData(BaseSchema):
    pass


class InvoicePdfReq(BaseSchema):
    pass


class InvoicePdfResponse(BaseSchema):
    pass


class IsCnRefundMethodData(BaseSchema):
    pass


class IsCnRefundMethodReq(BaseSchema):
    pass


class IsCnRefundMethodResponseData(BaseSchema):
    pass


class IsCnRefundMethodResponse(BaseSchema):
    pass


class CreditNoteConfigNotificationEvents(BaseSchema):
    pass


class CreateSellerCreditNoteConfig(BaseSchema):
    pass


class CreateSellerCreditNoteConfigReq(BaseSchema):
    pass


class CreateSellerCreditNoteConfigResponse(BaseSchema):
    pass


class DeleteConfig(BaseSchema):
    pass


class DeleteConfigReq(BaseSchema):
    pass


class DeleteConfigResponse(BaseSchema):
    pass


class ChannelDisplayNameItems(BaseSchema):
    pass


class ChannelDisplayNameResponse(BaseSchema):
    pass


class CnReferenceNumber(BaseSchema):
    pass


class GetPdfUrlViewReq(BaseSchema):
    pass


class GetPdfUrlViewResponseData(BaseSchema):
    pass


class GetPdfUrlViewResponse(BaseSchema):
    pass


class CreditNoteDetailsReq(BaseSchema):
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


class GetCustomerCreditBalanceReq(BaseSchema):
    pass


class GetCustomerCreditBalanceResponseData(BaseSchema):
    pass


class GetCustomerCreditBalanceResponse(BaseSchema):
    pass


class GetCnConfigReq(BaseSchema):
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


class GenerateReportCustomerCnReq(BaseSchema):
    pass


class CnGenerateReportItems(BaseSchema):
    pass


class GenerateReportCustomerCnResponseData(BaseSchema):
    pass


class GenerateReportCustomerCnResponse(BaseSchema):
    pass


class CnDownloadReport(BaseSchema):
    pass


class DownloadReportCustomerCnReq(BaseSchema):
    pass


class DownloadReportResponseData(BaseSchema):
    pass


class DownloadReportCustomerCnResponse(BaseSchema):
    pass


class GetReportingFilters(BaseSchema):
    pass


class GetReportingNestedFilters(BaseSchema):
    pass


class GetReportingFiltersReasonOptions(BaseSchema):
    pass


class GetReportingFiltersReason(BaseSchema):
    pass


class GetReportingFiltersResponse(BaseSchema):
    pass


class InvoicePaymentOptionsPayloadData(BaseSchema):
    pass


class InvoicePaymentOptionsReq(BaseSchema):
    pass


class InvoicePaymentOptionsResponsePayableAmounts(BaseSchema):
    pass


class InvoicePaymentOptionsResponseDeductedAmounts(BaseSchema):
    pass


class InvoicePaymentOptionsResponseData(BaseSchema):
    pass


class InvoicePaymentOptionsResponse(BaseSchema):
    pass


class PaymentDetail(BaseSchema):
    pass


class PaidInvoicePaymentDetail(BaseSchema):
    pass


class InvoicePaymentDetailsResponseData(BaseSchema):
    pass


class InvoicePaymentDetailsResponse(BaseSchema):
    pass


class InvoiceActivityLogsResponseData(BaseSchema):
    pass


class InvoiceActivityLogsResponse(BaseSchema):
    pass


class InvoiceActivityLogError(BaseSchema):
    pass


class UnlockCreditNoteRequestData(BaseSchema):
    pass


class UnlockCreditNoteReq(BaseSchema):
    pass


class UnlockCreditNoteResponseData(BaseSchema):
    pass


class UnlockCreditNoteResponse(BaseSchema):
    pass





class OrederFreezeResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    oms_freeze = fields.Boolean(required=False)
    
    source = fields.Str(required=False, allow_none=True)
    


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
    


class GenerateReportReq(BaseSchema):
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
    


class Currency(BaseSchema):
    # Finance swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class GenerateReportJson(BaseSchema):
    # Finance swagger.json

    
    data = fields.Dict(required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    items = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    


class Error(BaseSchema):
    # Finance swagger.json

    
    status = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False, allow_none=True)
    
    request_id = fields.Str(required=False, allow_none=True)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    
    meta = fields.Nested(ErrorMeta, required=False)
    


class ErrorMeta(BaseSchema):
    # Finance swagger.json

    
    columns_errors = fields.List(fields.Nested(ErrorMetaItems, required=False), required=False)
    


class ErrorMetaItems(BaseSchema):
    # Finance swagger.json

    
    code = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class DownloadReport(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DownloadReportData, required=False)
    


class DownloadReportData(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    
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
    


class GetEngineFilters(BaseSchema):
    # Finance swagger.json

    
    config_field = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    seller_id = fields.Str(required=False)
    


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    status = fields.Str(required=False)
    
    filters = fields.Nested(GetEngineFilters, required=False)
    
    project = fields.List(fields.Str(required=False), required=False)
    
    table_name = fields.Str(required=False)
    
    search = fields.Dict(required=False)
    
    page = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    
    order_by = fields.Str(required=False)
    


class GetEngineReq(BaseSchema):
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
    


class GetReasonReq(BaseSchema):
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
    


class GetReportListReq(BaseSchema):
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
    
    display_date = fields.Str(required=False, allow_none=True)
    


class GetAffiliateResponse(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    docs = fields.List(fields.Dict(required=False), required=False)
    


class DownloadCreditDebitNote(BaseSchema):
    # Finance swagger.json

    
    note_id = fields.List(fields.Str(required=False), required=False)
    


class DownloadCreditDebitNoteReq(BaseSchema):
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
    
    amount = fields.Float(required=False)
    
    transaction_type = fields.Str(required=False)
    
    source_reference = fields.Str(required=False)
    
    total_amount = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    seller_id = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    


class PaymentProcessReq(BaseSchema):
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
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    


class CreditlineDataPlatformReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CreditlineDataPlatformPayload, required=False)
    


class CreditlineDataPlatformResponse(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    code = fields.Int(required=False)
    
    show_mr = fields.Boolean(required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    item_count = fields.Int(required=False)
    


class IsCreditlinePayload(BaseSchema):
    # Finance swagger.json

    
    seller_id = fields.Str(required=False)
    


class IsCreditlinePlatformReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(IsCreditlinePayload, required=False)
    


class IsCreditlinePlatformResponse(BaseSchema):
    # Finance swagger.json

    
    is_creditline_opted = fields.Boolean(required=False)
    
    code = fields.Int(required=False)
    


class InvoiceTypePayloadData(BaseSchema):
    # Finance swagger.json

    
    is_active = fields.Boolean(required=False)
    


class InvoiceTypeReq(BaseSchema):
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
    


class InvoiceListingReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoiceListingPayloadData, required=False)
    


class UnpaidInvoiceDataItems(BaseSchema):
    # Finance swagger.json

    
    total_unpaid_invoice_count = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    total_unpaid_amount = fields.Float(required=False)
    


class InvoiceListingResponseItems(BaseSchema):
    # Finance swagger.json

    
    amount = fields.Float(required=False)
    
    company = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    
    period = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    
    is_downloadable = fields.Boolean(required=False)
    
    invoice_id = fields.Str(required=False)
    
    currency = fields.Nested(Currency, required=False)
    


class InvoiceListingResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    unpaid_invoice_data = fields.Nested(UnpaidInvoiceDataItems, required=False)
    
    items = fields.List(fields.Nested(InvoiceListingResponseItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    


class InvoicePdfPayloadData(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.List(fields.Str(required=False), required=False)
    


class InvoicePdfReq(BaseSchema):
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
    


class IsCnRefundMethodReq(BaseSchema):
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
    


class CreateSellerCreditNoteConfigReq(BaseSchema):
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
    


class DeleteConfigReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DeleteConfig, required=False)
    


class DeleteConfigResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ChannelDisplayNameItems(BaseSchema):
    # Finance swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ChannelDisplayNameResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(ChannelDisplayNameItems, required=False), required=False)
    


class CnReferenceNumber(BaseSchema):
    # Finance swagger.json

    
    cn_reference_number = fields.Str(required=False)
    


class GetPdfUrlViewReq(BaseSchema):
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
    


class CreditNoteDetailsReq(BaseSchema):
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

    
    meta = fields.Dict(required=False)
    
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

    
    currency = fields.Str(required=False, allow_none=True)
    
    current_amount_used = fields.Float(required=False)
    
    cn_status = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    
    cn_reference_number = fields.Str(required=False)
    
    cn_details = fields.Nested(CnDetails, required=False)
    
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
    


class GetCustomerCreditBalanceReq(BaseSchema):
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
    


class GetCnConfigReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DeleteConfig, required=False)
    


class GetCnConfigResponseMeta(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False, allow_none=True)
    
    source_channel = fields.List(fields.Str(required=False), required=False)
    


class GetCnConfigResponseData(BaseSchema):
    # Finance swagger.json

    
    is_cn_as_refund_method = fields.Boolean(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    meta = fields.Raw(required=False)
    
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
    
    type_of_transaction = fields.List(fields.Str(required=False), required=False)
    
    issuance_channel = fields.List(fields.Str(required=False), required=False)
    


class CnGenerateReport(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    
    filters = fields.Nested(CnGenerateReportFilters, required=False)
    
    affiliate_id = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportFilters, required=False)
    
    search = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    search_type = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    


class GenerateReportCustomerCnReq(BaseSchema):
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

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
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
    
    status = fields.Str(required=False)
    
    search_type = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    


class DownloadReportCustomerCnReq(BaseSchema):
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

    
    items = fields.List(fields.Nested(DownloadReportResponseData, required=False), required=False)
    
    data = fields.List(fields.Nested(DownloadReportResponseData, required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    


class GetReportingFiltersReasonOptions(BaseSchema):
    # Finance swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    placeholder_text = fields.Str(required=False)
    


class GetReportingFiltersReason(BaseSchema):
    # Finance swagger.json

    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(GetReportingFiltersReasonOptions, required=False), required=False)
    


class GetReportingFiltersResponse(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Nested(GetReportingFiltersReason, required=False)
    
    search = fields.Nested(GetReportingFilters, required=False)
    
    filters = fields.List(fields.Nested(GetReportingNestedFilters, required=False), required=False)
    
    status = fields.Nested(GetReportingFilters, required=False)
    


class InvoicePaymentOptionsPayloadData(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.Str(required=False)
    


class InvoicePaymentOptionsReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoicePaymentOptionsPayloadData, required=False)
    


class InvoicePaymentOptionsResponsePayableAmounts(BaseSchema):
    # Finance swagger.json

    
    amount = fields.Float(required=False)
    
    amount_key = fields.Str(required=False)
    
    header = fields.Str(required=False)
    


class InvoicePaymentOptionsResponseDeductedAmounts(BaseSchema):
    # Finance swagger.json

    
    amount = fields.Float(required=False)
    
    header = fields.Str(required=False)
    
    amount_key = fields.Str(required=False)
    
    is_payable = fields.Boolean(required=False)
    
    symbol = fields.Str(required=False)
    


class InvoicePaymentOptionsResponseData(BaseSchema):
    # Finance swagger.json

    
    currency = fields.Nested(Currency, required=False)
    
    invoice_type = fields.Str(required=False)
    
    display_amounts = fields.List(fields.Nested(InvoicePaymentOptionsResponsePayableAmounts, required=False), required=False)
    
    total_amount = fields.Dict(required=False)
    
    deducted_amounts = fields.Raw(required=False)
    
    payable_amounts = fields.List(fields.Nested(InvoicePaymentOptionsResponsePayableAmounts, required=False), required=False)
    


class InvoicePaymentOptionsResponse(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    data = fields.Nested(InvoicePaymentOptionsResponseData, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentDetail(BaseSchema):
    # Finance swagger.json

    
    display_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class PaidInvoicePaymentDetail(BaseSchema):
    # Finance swagger.json

    
    payment_details = fields.List(fields.Nested(PaymentDetail, required=False), required=False)
    
    date_of_payment = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class InvoicePaymentDetailsResponseData(BaseSchema):
    # Finance swagger.json

    
    paid_invoice_payment_details = fields.List(fields.Nested(PaidInvoicePaymentDetail, required=False), required=False)
    
    failed_attempts_details = fields.List(fields.Dict(required=False), required=False)
    


class InvoicePaymentDetailsResponse(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    data = fields.Nested(InvoicePaymentDetailsResponseData, required=False)
    
    success = fields.Boolean(required=False)
    
    payment_details_visible = fields.Boolean(required=False)
    


class InvoiceActivityLogsResponseData(BaseSchema):
    # Finance swagger.json

    
    performed_by = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    
    reason = fields.Str(required=False, allow_none=True)
    
    is_resolved = fields.Boolean(required=False)
    
    retry_attempts = fields.Float(required=False)
    
    max_retry_attempts = fields.Float(required=False, allow_none=True)
    


class InvoiceActivityLogsResponse(BaseSchema):
    # Finance swagger.json

    
    data = fields.List(fields.Nested(InvoiceActivityLogsResponseData, required=False), required=False)
    


class InvoiceActivityLogError(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    


class UnlockCreditNoteRequestData(BaseSchema):
    # Finance swagger.json

    
    seller_id = fields.Str(required=False)
    
    locked_credit_notes = fields.List(fields.Str(required=False), required=False)
    
    unlock_reason = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class UnlockCreditNoteReq(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(UnlockCreditNoteRequestData, required=False)
    


class UnlockCreditNoteResponseData(BaseSchema):
    # Finance swagger.json

    
    is_cn_unlocked = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    


class UnlockCreditNoteResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(UnlockCreditNoteResponseData, required=False)
    


