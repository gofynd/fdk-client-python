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


class GetEngineFilters(BaseSchema):
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


class GetDocs(BaseSchema):
    pass


class GetReasonResponse(BaseSchema):
    pass


class GetReportListData(BaseSchema):
    pass


class GetReportListRequest(BaseSchema):
    pass


class GetAffiliate(BaseSchema):
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


class InvoiceListingResponseItems(BaseSchema):
    pass


class UnpaidInvoiceDataItems(BaseSchema):
    pass


class InvoiceListingResponse(BaseSchema):
    pass


class InvoicePdfPayloadData(BaseSchema):
    pass


class InvoicePdfRequest(BaseSchema):
    pass


class InvoicePdfResponse(BaseSchema):
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

    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    start_date = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    end_date = fields.Str(required=False)
    


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

    
    start_date = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    items = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    


class Error(BaseSchema):
    # Finance swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class DownloadReport(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    


class DownloadReportItems(BaseSchema):
    # Finance swagger.json

    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    type_of_request = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    end_date = fields.Str(required=False)
    


class DownloadReportList(BaseSchema):
    # Finance swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(DownloadReportItems, required=False), required=False)
    
    item_count = fields.Int(required=False)
    


class GetEngineFilters(BaseSchema):
    # Finance swagger.json

    
    config_field = fields.Str(required=False)
    


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    filters = fields.Nested(GetEngineFilters, required=False)
    
    project = fields.List(fields.Str(required=False), required=False)
    
    table_name = fields.Str(required=False)
    


class GetEngineRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetEngineData, required=False)
    


class GetEngineResponse(BaseSchema):
    # Finance swagger.json

    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    item_count = fields.Int(required=False)
    


class GetReason(BaseSchema):
    # Finance swagger.json

    
    reason_type = fields.Str(required=False)
    


class GetReasonRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReason, required=False)
    


class GetDocs(BaseSchema):
    # Finance swagger.json

    
    docs = fields.List(fields.Dict(required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


class GetReasonResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(GetDocs, required=False)
    


class GetReportListData(BaseSchema):
    # Finance swagger.json

    
    listing_enabled = fields.Boolean(required=False)
    
    role_name = fields.Str(required=False)
    


class GetReportListRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReportListData, required=False)
    


class GetAffiliate(BaseSchema):
    # Finance swagger.json

    
    company_id = fields.Int(required=False)
    


class GetAffiliateResponse(BaseSchema):
    # Finance swagger.json

    
    docs = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class DownloadCreditDebitNote(BaseSchema):
    # Finance swagger.json

    
    note_id = fields.List(fields.Str(required=False), required=False)
    


class DownloadCreditDebitNoteRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(DownloadCreditDebitNote, required=False)
    


class DownloadCreditDebitNoteResponseData(BaseSchema):
    # Finance swagger.json

    
    pdf_s3_url = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class DownloadCreditDebitNoteResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(DownloadCreditDebitNoteResponseData, required=False), required=False)
    


class PaymentProcessPayload(BaseSchema):
    # Finance swagger.json

    
    meta = fields.Dict(required=False)
    
    amount = fields.Str(required=False)
    
    transaction_type = fields.Str(required=False)
    
    seller_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    source_reference = fields.Str(required=False)
    
    total_amount = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    


class PaymentProcessRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(PaymentProcessPayload, required=False)
    


class PaymentProcessResponse(BaseSchema):
    # Finance swagger.json

    
    meta = fields.Dict(required=False)
    
    redirect_url = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Int(required=False)
    


class CreditlineDataPlatformPayload(BaseSchema):
    # Finance swagger.json

    
    page = fields.Int(required=False)
    
    seller_id = fields.Str(required=False)
    
    start_end = fields.Str(required=False)
    
    end_end = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    


class CreditlineDataPlatformRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CreditlineDataPlatformPayload, required=False)
    


class CreditlineDataPlatformResponse(BaseSchema):
    # Finance swagger.json

    
    page = fields.Dict(required=False)
    
    show_mr = fields.Boolean(required=False)
    
    item_count = fields.Int(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    code = fields.Int(required=False)
    


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

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    


class InvoiceTypeResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    payment_status_list = fields.List(fields.Nested(InvoiceTypeResponseItems, required=False), required=False)
    
    invoice_type_list = fields.List(fields.Nested(InvoiceTypeResponseItems, required=False), required=False)
    


class InoviceListingPayloadDataFilters(BaseSchema):
    # Finance swagger.json

    
    payment_status = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.List(fields.Str(required=False), required=False)
    
    invoice_type = fields.List(fields.Str(required=False), required=False)
    


class InvoiceListingPayloadData(BaseSchema):
    # Finance swagger.json

    
    page_size = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    page = fields.Int(required=False)
    
    search = fields.Str(required=False)
    
    filters = fields.Nested(InoviceListingPayloadDataFilters, required=False)
    
    end_date = fields.Str(required=False)
    


class InvoiceListingRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoiceListingPayloadData, required=False)
    


class InvoiceListingResponseItems(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    
    is_downloadable = fields.Boolean(required=False)
    
    invoice_type = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    period = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    


class UnpaidInvoiceDataItems(BaseSchema):
    # Finance swagger.json

    
    currency = fields.Str(required=False)
    
    total_unpaid_invoice_count = fields.Int(required=False)
    
    total_unpaid_amount = fields.Float(required=False)
    


class InvoiceListingResponse(BaseSchema):
    # Finance swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(InvoiceListingResponseItems, required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    unpaid_invoice_data = fields.Nested(UnpaidInvoiceDataItems, required=False)
    


class InvoicePdfPayloadData(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.List(fields.Str(required=False), required=False)
    


class InvoicePdfRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoicePdfPayloadData, required=False)
    


class InvoicePdfResponse(BaseSchema):
    # Finance swagger.json

    
    error = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Str(required=False), required=False)
    


