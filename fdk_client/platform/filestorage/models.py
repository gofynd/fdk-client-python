"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class FailedResponse(BaseSchema):
    pass


class CDN(BaseSchema):
    pass


class Upload(BaseSchema):
    pass


class StartResponse(BaseSchema):
    pass


class StartRequest(BaseSchema):
    pass


class CompleteResponse(BaseSchema):
    pass


class Opts(BaseSchema):
    pass


class CopyFileTask(BaseSchema):
    pass


class BulkUploadResponse(BaseSchema):
    pass


class Destination(BaseSchema):
    pass


class BulkRequest(BaseSchema):
    pass


class DestinationNamespace(BaseSchema):
    pass


class CopyFiles(BaseSchema):
    pass


class DestinationBasepath(BaseSchema):
    pass


class CopyFilesWithRewrite(BaseSchema):
    pass


class Urls(BaseSchema):
    pass


class SignUrlResponse(BaseSchema):
    pass


class SignUrlRequest(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class DbRecord(BaseSchema):
    pass


class BrowseResponse(BaseSchema):
    pass


class InvoiceTypesResponse(BaseSchema):
    pass


class payments(BaseSchema):
    pass


class invoiceDetail(BaseSchema):
    pass


class companyDetail(BaseSchema):
    pass


class storeDetail(BaseSchema):
    pass


class customerShippingDetail(BaseSchema):
    pass


class Brand(BaseSchema):
    pass


class Products(BaseSchema):
    pass


class productTable(BaseSchema):
    pass


class returnDetail(BaseSchema):
    pass


class TaxeItems(BaseSchema):
    pass


class taxTable(BaseSchema):
    pass


class customerBillingDetail(BaseSchema):
    pass


class registeredCompanyDetail(BaseSchema):
    pass


class DummyTemplateDataPayloadImage(BaseSchema):
    pass


class DummyTemplateDataPayload(BaseSchema):
    pass


class DummyTemplateDataItems(BaseSchema):
    pass


class Status(BaseSchema):
    pass


class FileSrc(BaseSchema):
    pass


class File(BaseSchema):
    pass


class FilesSuccess(BaseSchema):
    pass


class BulkUploadSyncMode(BaseSchema):
    pass


class BulkUploadFailFileResponseItems(BaseSchema):
    pass


class BulkUploadFailResponse(BaseSchema):
    pass


class pdfRender(BaseSchema):
    pass


class pdfConfig(BaseSchema):
    pass





class FailedResponse(BaseSchema):
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
    


class StartResponse(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class StartRequest(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    params = fields.Dict(required=False)
    


class CompleteResponse(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class Opts(BaseSchema):
    # FileStorage swagger.json

    
    attempts = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    


class CopyFileTask(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    data = fields.Nested(BulkRequest, required=False)
    
    opts = fields.Nested(Opts, required=False)
    
    progress = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    attempts_made = fields.Int(required=False)
    
    stacktrace = fields.List(fields.Str(required=False), required=False)
    
    finished_on = fields.Int(required=False)
    
    processed_on = fields.Int(required=False)
    


class BulkUploadResponse(BaseSchema):
    # FileStorage swagger.json

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    


class Destination(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    
    rewrite = fields.Str(required=False)
    
    basepath = fields.Str(required=False)
    


class BulkRequest(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(Destination, required=False)
    


class DestinationNamespace(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    


class CopyFiles(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(DestinationNamespace, required=False)
    


class DestinationBasepath(BaseSchema):
    # FileStorage swagger.json

    
    basepath = fields.Str(required=False)
    
    rewrite = fields.Str(required=False)
    


class CopyFilesWithRewrite(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(DestinationBasepath, required=False)
    


class Urls(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    signed_url = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    


class SignUrlResponse(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    


class SignUrlRequest(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    urls = fields.List(fields.Str(required=False), required=False)
    


class Page(BaseSchema):
    # FileStorage swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class DbRecord(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class BrowseResponse(BaseSchema):
    # FileStorage swagger.json

    
    items = fields.List(fields.Nested(DbRecord, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class InvoiceTypesResponse(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    format = fields.List(fields.Str(required=False), required=False)
    
    __v = fields.Int(required=False)
    
    visibility = fields.Boolean(required=False)
    
    schema = fields.Dict(required=False)
    


class payments(BaseSchema):
    # FileStorage swagger.json

    
    payment_type = fields.Str(required=False)
    
    date = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class invoiceDetail(BaseSchema):
    # FileStorage swagger.json

    
    invoice_id = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    
    irn = fields.Str(required=False)
    
    external_order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    channel_order_id = fields.Str(required=False)
    


class companyDetail(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pan = fields.Str(required=False)
    
    phone_no = fields.Str(required=False)
    
    cin = fields.Str(required=False)
    
    website_url = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class storeDetail(BaseSchema):
    # FileStorage swagger.json

    
    store_name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    


class customerShippingDetail(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    phone_no = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    


class Brand(BaseSchema):
    # FileStorage swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Products(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    total_units = fields.Float(required=False)
    
    mrp = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    taxable_amount = fields.Float(required=False)
    
    total_taxable_amount = fields.Float(required=False)
    
    tax = fields.Dict(required=False)
    
    total = fields.Float(required=False)
    
    brand = fields.Nested(Brand, required=False)
    


class productTable(BaseSchema):
    # FileStorage swagger.json

    
    total_items = fields.Float(required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    grand_total = fields.Float(required=False)
    
    delivery_charges = fields.Str(required=False)
    
    delivery_charge_text = fields.Str(required=False)
    
    cod_charges = fields.Str(required=False)
    
    fynd_discounts = fields.Str(required=False)
    
    total_in_words = fields.Str(required=False)
    


class returnDetail(BaseSchema):
    # FileStorage swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    


class TaxeItems(BaseSchema):
    # FileStorage swagger.json

    
    hsn_code = fields.Str(required=False)
    
    tax = fields.Dict(required=False)
    
    total = fields.Float(required=False)
    


class taxTable(BaseSchema):
    # FileStorage swagger.json

    
    taxes = fields.List(fields.Nested(TaxeItems, required=False), required=False)
    
    grand_total = fields.Float(required=False)
    
    tax_in_words = fields.Str(required=False)
    


class customerBillingDetail(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    phone_no = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class registeredCompanyDetail(BaseSchema):
    # FileStorage swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class DummyTemplateDataPayloadImage(BaseSchema):
    # FileStorage swagger.json

    
    sales_channel_logo = fields.Str(required=False)
    


class DummyTemplateDataPayload(BaseSchema):
    # FileStorage swagger.json

    
    currency_code = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    amount_to_be_collected = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    awb_number_barcode = fields.Str(required=False)
    
    signed_qrcode = fields.Str(required=False)
    
    shipment_id_barcode = fields.Str(required=False)
    
    upi_qrcode = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    is_self_pickup = fields.Boolean(required=False)
    
    is_test = fields.Boolean(required=False)
    
    image = fields.Nested(DummyTemplateDataPayloadImage, required=False)
    
    payments = fields.List(fields.Nested(payments, required=False), required=False)
    
    invoice_detail = fields.Raw(required=False)
    
    company_detail = fields.Nested(companyDetail, required=False)
    
    store_detail = fields.Nested(storeDetail, required=False)
    
    customer_shipping_detail = fields.Nested(customerShippingDetail, required=False)
    
    return_detail = fields.Nested(returnDetail, required=False)
    
    product_table = fields.Nested(productTable, required=False)
    
    tax_table = fields.Nested(taxTable, required=False)
    
    declaration_texts = fields.List(fields.Str(required=False), required=False)
    
    registered_company_detail = fields.Nested(registeredCompanyDetail, required=False)
    
    disclaimer = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    delivery_partner_detail = fields.Dict(required=False)
    
    customer_billing_detail = fields.Nested(customerBillingDetail, required=False)
    


class DummyTemplateDataItems(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Float(required=False)
    
    payload = fields.Nested(DummyTemplateDataPayload, required=False)
    
    __v = fields.Int(required=False)
    


class Status(BaseSchema):
    # FileStorage swagger.json

    
    total = fields.Float(required=False)
    
    failed = fields.Float(required=False)
    
    succeeded = fields.Float(required=False)
    
    result = fields.Str(required=False)
    


class FileSrc(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    


class File(BaseSchema):
    # FileStorage swagger.json

    
    src = fields.Nested(FileSrc, required=False)
    


class FilesSuccess(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    file = fields.Nested(File, required=False)
    


class BulkUploadSyncMode(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Nested(Status, required=False)
    
    files = fields.List(fields.Nested(FilesSuccess, required=False), required=False)
    


class BulkUploadFailFileResponseItems(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    
    file = fields.Nested(File, required=False)
    
    stage = fields.Str(required=False)
    


class BulkUploadFailResponse(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Nested(Status, required=False)
    
    files = fields.List(fields.Raw(required=False), required=False)
    


class pdfRender(BaseSchema):
    # FileStorage swagger.json

    
    format = fields.Str(required=False)
    
    payload = fields.List(fields.Nested(DummyTemplateDataItems, required=False), required=False)
    
    template = fields.Str(required=False)
    


class pdfConfig(BaseSchema):
    # FileStorage swagger.json

    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    


