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


class DownloadCreditDebitNoteResponse(BaseSchema):
    pass


class PaymentProcessPayload(BaseSchema):
    pass


class PaymentProcessRequest(BaseSchema):
    pass


class PaymentProcessResponse(BaseSchema):
    pass





class GenerateReportMeta(BaseSchema):
    # Finance swagger.json

    
    company = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    


class GenerateReportFilters(BaseSchema):
    # Finance swagger.json

    
    company = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    
    channel = fields.List(fields.Str(required=False), required=False)
    


class GenerateReportPlatform(BaseSchema):
    # Finance swagger.json

    
    start_date = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    report_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
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
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    start_date = fields.Str(required=False)
    
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
    
    start_date = fields.Str(required=False)
    
    pagesize = fields.Int(required=False)
    


class DownloadReportItems(BaseSchema):
    # Finance swagger.json

    
    start_date = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    end_date = fields.Str(required=False)
    
    type_of_request = fields.Str(required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    


class DownloadReportList(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Nested(DownloadReportItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    


class GetEngineFilters(BaseSchema):
    # Finance swagger.json

    
    config_field = fields.Str(required=False)
    


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    project = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(GetEngineFilters, required=False)
    
    table_name = fields.Str(required=False)
    


class GetEngineRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetEngineData, required=False)
    


class GetEngineResponse(BaseSchema):
    # Finance swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    item_count = fields.Int(required=False)
    


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

    
    data = fields.Nested(GetDocs, required=False)
    
    success = fields.Boolean(required=False)
    


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
    


class DownloadCreditDebitNoteResponse(BaseSchema):
    # Finance swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentProcessPayload(BaseSchema):
    # Finance swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    seller_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    amount = fields.Str(required=False)
    
    transaction_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    total_amount = fields.Str(required=False)
    
    source_reference = fields.Str(required=False)
    
    invoice_number = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    


class PaymentProcessRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(PaymentProcessPayload, required=False)
    


class PaymentProcessResponse(BaseSchema):
    # Finance swagger.json

    
    meta = fields.Dict(required=False)
    
    redirect_url = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


