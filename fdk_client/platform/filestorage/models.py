"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class FailedBrowseFilesResult(BaseSchema):
    pass


class CDN(BaseSchema):
    pass


class Upload(BaseSchema):
    pass


class FileUpload(BaseSchema):
    pass


class FileUploadStart(BaseSchema):
    pass


class CreatedBy(BaseSchema):
    pass


class FileUploadComplete(BaseSchema):
    pass


class ProxyFileAccess(BaseSchema):
    pass


class DestinationNamespace(BaseSchema):
    pass


class CopyFiles(BaseSchema):
    pass


class Urls(BaseSchema):
    pass


class SignUrlResult(BaseSchema):
    pass


class SignUrl(BaseSchema):
    pass


class PdfConfig(BaseSchema):
    pass


class PdfConfigSuccessData(BaseSchema):
    pass


class PdfConfigSuccess(BaseSchema):
    pass


class PdfConfigSaveSuccessData(BaseSchema):
    pass


class PdfConfigSaveSuccess(BaseSchema):
    pass


class PaymentReceiptRequestBody(BaseSchema):
    pass


class PaymentReceiptOrderDetails(BaseSchema):
    pass


class PaymentReceiptCustomerDetails(BaseSchema):
    pass


class PaymentReceiptPayments(BaseSchema):
    pass


class PaymentReceiptFormat(BaseSchema):
    pass


class PaymentReceiptService(BaseSchema):
    pass


class PaymentReceiptTaxes(BaseSchema):
    pass


class PaymentReceiptPayload(BaseSchema):
    pass


class PaymentReceiptMeta(BaseSchema):
    pass


class ExtensionSlug(BaseSchema):
    pass





class FailedBrowseFilesResult(BaseSchema):
    # FileStorage swagger.json

    
    message = fields.Str(required=False)
    


class CDN(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    absolute_url = fields.Str(required=False)
    
    relative_url = fields.Str(required=False)
    


class Upload(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class FileUpload(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class FileUploadStart(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    params = fields.Dict(required=False)
    


class CreatedBy(BaseSchema):
    # FileStorage swagger.json

    
    username = fields.Str(required=False)
    


class FileUploadComplete(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    


class ProxyFileAccess(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    


class DestinationNamespace(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    


class CopyFiles(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(DestinationNamespace, required=False)
    


class Urls(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    signed_url = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    


class SignUrlResult(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    


class SignUrl(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    urls = fields.List(fields.Str(required=False), required=False)
    


class PdfConfig(BaseSchema):
    # FileStorage swagger.json

    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
    default_template = fields.Boolean(required=False)
    


class PdfConfigSuccessData(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    


class PdfConfigSuccess(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.List(fields.Nested(PdfConfigSuccessData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class PdfConfigSaveSuccessData(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class PdfConfigSaveSuccess(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.Nested(PdfConfigSaveSuccessData, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentReceiptRequestBody(BaseSchema):
    # FileStorage swagger.json

    
    payload = fields.Nested(PaymentReceiptPayload, required=False)
    
    meta = fields.Nested(PaymentReceiptMeta, required=False)
    


class PaymentReceiptOrderDetails(BaseSchema):
    # FileStorage swagger.json

    
    jiomart_order_id = fields.Str(required=False)
    
    total_items = fields.Float(required=False)
    
    final_amount = fields.Float(required=False)
    
    final_amount_in_words = fields.Str(required=False)
    
    order_created_date = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    prm_id = fields.Str(required=False)
    
    receipt_no = fields.Str(required=False)
    
    taxes = fields.Nested(PaymentReceiptTaxes, required=False)
    


class PaymentReceiptCustomerDetails(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    


class PaymentReceiptPayments(BaseSchema):
    # FileStorage swagger.json

    
    payment_desc = fields.Str(required=False)
    
    txn_date = fields.Str(required=False)
    


class PaymentReceiptFormat(BaseSchema):
    # FileStorage swagger.json

    
    payment_receipt = fields.List(fields.Str(required=False), required=False)
    


class PaymentReceiptService(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    


class PaymentReceiptTaxes(BaseSchema):
    # FileStorage swagger.json

    
    gstin = fields.Str(required=False)
    
    pancard = fields.Str(required=False)
    


class PaymentReceiptPayload(BaseSchema):
    # FileStorage swagger.json

    
    uid = fields.Str(required=False)
    
    order_detail = fields.Nested(PaymentReceiptOrderDetails, required=False)
    
    customer_detail = fields.Nested(PaymentReceiptCustomerDetails, required=False)
    
    payments = fields.List(fields.Nested(PaymentReceiptPayments, required=False), required=False)
    


class PaymentReceiptMeta(BaseSchema):
    # FileStorage swagger.json

    
    job_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    event = fields.Dict(required=False)
    
    organizaton_id = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    format = fields.Nested(PaymentReceiptFormat, required=False)
    
    trace_id = fields.List(fields.Str(required=False), required=False)
    
    created_timestamp = fields.Float(required=False)
    
    service = fields.Nested(PaymentReceiptService, required=False)
    
    event_trace_info = fields.Dict(required=False)
    
    trace = fields.Str(required=False)
    


class ExtensionSlug(BaseSchema):
    # FileStorage swagger.json

    
    extension_slug = fields.Str(required=False)
    


