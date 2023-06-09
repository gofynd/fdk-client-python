"""Finance Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class GenerateReportFilters(BaseSchema):
    pass


class GenerateReportMeta(BaseSchema):
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


class GetInvoiceListPayloadData(BaseSchema):
    pass


class GetInvoiceListRequest(BaseSchema):
    pass


class GetInvoiceListResponse(BaseSchema):
    pass


class InoviceListingPayloadDataFilters(BaseSchema):
    pass


class InvoiceListingPayloadData(BaseSchema):
    pass


class InvoiceListingRequest(BaseSchema):
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





class GenerateReportFilters(BaseSchema):
    # Finance swagger.json

    
    company = fields.List(fields.Str(required=False), required=False)
    
    channel = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    


class GenerateReportMeta(BaseSchema):
    # Finance swagger.json

    
    company = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    


class GenerateReportPlatform(BaseSchema):
    # Finance swagger.json

    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    end_date = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    start_date = fields.Str(required=False)
    


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

    
    end_date = fields.Str(required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    
    start_date = fields.Str(required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    items = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    


class Error(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    reason = fields.Str(required=False)
    


class DownloadReport(BaseSchema):
    # Finance swagger.json

    
    pagesize = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class DownloadReportItems(BaseSchema):
    # Finance swagger.json

    
    report_id = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    end_date = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    start_date = fields.Str(required=False)
    
    type_of_request = fields.Str(required=False)
    


class DownloadReportList(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Nested(DownloadReportItems, required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetEngineFilters(BaseSchema):
    # Finance swagger.json

    
    config_field = fields.Str(required=False)
    


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    table_name = fields.Str(required=False)
    
    project = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(GetEngineFilters, required=False)
    


class GetEngineRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetEngineData, required=False)
    


class GetEngineResponse(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetReason(BaseSchema):
    # Finance swagger.json

    
    reason_type = fields.Str(required=False)
    


class GetReasonRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReason, required=False)
    


class GetDocs(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    docs = fields.List(fields.Dict(required=False), required=False)
    


class GetReasonResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(GetDocs, required=False)
    


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

    
    currency = fields.Str(required=False)
    
    total_amount = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_id = fields.Str(required=False)
    
    source_reference = fields.Str(required=False)
    
    transaction_type = fields.Str(required=False)
    


class PaymentProcessRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(PaymentProcessPayload, required=False)
    


class PaymentProcessResponse(BaseSchema):
    # Finance swagger.json

    
    code = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    


class GetInvoiceListPayloadData(BaseSchema):
    # Finance swagger.json

    
    is_active = fields.Boolean(required=False)
    


class GetInvoiceListRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetInvoiceListPayloadData, required=False)
    


class GetInvoiceListResponse(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    payment_status_list = fields.List(fields.Dict(required=False), required=False)
    
    invoice_type_list = fields.List(fields.Dict(required=False), required=False)
    


class InoviceListingPayloadDataFilters(BaseSchema):
    # Finance swagger.json

    
    company_id = fields.List(fields.Str(required=False), required=False)
    
    invoice_type = fields.List(fields.Str(required=False), required=False)
    
    payment_status = fields.List(fields.Str(required=False), required=False)
    


class InvoiceListingPayloadData(BaseSchema):
    # Finance swagger.json

    
    filters = fields.Nested(InoviceListingPayloadDataFilters, required=False)
    
    page_size = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    
    page = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    search = fields.Str(required=False)
    


class InvoiceListingRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(InvoiceListingPayloadData, required=False)
    


class InvoiceListingResponseItems(BaseSchema):
    # Finance swagger.json

    
    invoice_number = fields.Str(required=False)
    
    period = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_downloadable = fields.Boolean(required=False)
    
    invoice_id = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    


class InvoiceListingResponse(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Nested(InvoiceListingResponseItems, required=False), required=False)
    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    


