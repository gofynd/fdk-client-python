"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class UpdatePdfTypeRequest(BaseSchema):
    pass


class PdfTypeIdResponse(BaseSchema):
    pass


class PdfConfigurationData(BaseSchema):
    pass


class PdfConfigurationResponse(BaseSchema):
    pass


class UpdateTemplate(BaseSchema):
    pass


class PdfDefaultTemplateResponse(BaseSchema):
    pass


class PdfTemplateCreateSuccess(BaseSchema):
    pass


class PdfTemplateCreateSuccessData(BaseSchema):
    pass


class CreateTemplate(BaseSchema):
    pass


class PdfDefaultTemplateSuccess(BaseSchema):
    pass


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


class CreatedBy(BaseSchema):
    pass


class CompleteResponse(BaseSchema):
    pass


class ProxyResponse(BaseSchema):
    pass


class DestinationNamespace(BaseSchema):
    pass


class CopyFiles(BaseSchema):
    pass


class Urls(BaseSchema):
    pass


class SignUrlResponse(BaseSchema):
    pass


class SignUrlRequest(BaseSchema):
    pass


class InvoiceTypesDataResponse(BaseSchema):
    pass


class InvoiceTypesResponse(BaseSchema):
    pass


class ConversionRate(BaseSchema):
    pass


class DeliveryPartnerDetail(BaseSchema):
    pass


class Image(BaseSchema):
    pass


class PaymentData(BaseSchema):
    pass


class InvoiceDetail(BaseSchema):
    pass


class CompanyDetail(BaseSchema):
    pass


class StoreDetail(BaseSchema):
    pass


class CustomerBillingDetail(BaseSchema):
    pass


class CustomerShippingDetail(BaseSchema):
    pass


class ReturnDetail(BaseSchema):
    pass


class Brand(BaseSchema):
    pass


class Cgst(BaseSchema):
    pass


class Sgst(BaseSchema):
    pass


class Igst(BaseSchema):
    pass


class Tax(BaseSchema):
    pass


class ItemsProductTable(BaseSchema):
    pass


class ProductTable(BaseSchema):
    pass


class Taxes(BaseSchema):
    pass


class TaxTable(BaseSchema):
    pass


class RegisteredCompanyDetail(BaseSchema):
    pass


class Kwargs(BaseSchema):
    pass


class ShipmentIdBarcodeGenerator(BaseSchema):
    pass


class SignedQrcodeGenerator(BaseSchema):
    pass


class KwargsUpiQrcode(BaseSchema):
    pass


class UpiQrcodeGenerator(BaseSchema):
    pass


class DigitalsignatureGenerator(BaseSchema):
    pass


class KwargsAwbNumber(BaseSchema):
    pass


class AwbNumberLabelBarcodeGenerator(BaseSchema):
    pass


class AwbNumberBarcodeGenerator(BaseSchema):
    pass


class MetaProperty(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class DummyTemplateDataPayload(BaseSchema):
    pass


class DummyTemplateData(BaseSchema):
    pass


class savePdfPayload(BaseSchema):
    pass


class DummyPayloadById(BaseSchema):
    pass


class DummyTemplateDataItems(BaseSchema):
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


class Document(BaseSchema):
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





class UpdatePdfTypeRequest(BaseSchema):
    # FileStorage swagger.json

    
    pdf_type_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    format = fields.List(fields.Str(required=False), required=False)
    
    visibility = fields.Boolean(required=False)
    
    schema = fields.Dict(required=False)
    
    store_os = fields.Boolean(required=False)
    
    country_code = fields.Str(required=False)
    


class PdfTypeIdResponse(BaseSchema):
    # FileStorage swagger.json

    
    store_os = fields.Boolean(required=False)
    
    country_code = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    __v = fields.Int(required=False)
    
    format = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    visibility = fields.Boolean(required=False)
    


class PdfConfigurationData(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class PdfConfigurationResponse(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.Nested(PdfConfigurationData, required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateTemplate(BaseSchema):
    # FileStorage swagger.json

    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    store_os = fields.Boolean(required=False)
    


class PdfDefaultTemplateResponse(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    format = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    __v = fields.Int(required=False)
    
    template = fields.Str(required=False)
    


class PdfTemplateCreateSuccess(BaseSchema):
    # FileStorage swagger.json

    
    code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(PdfTemplateCreateSuccessData, required=False)
    


class PdfTemplateCreateSuccessData(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class CreateTemplate(BaseSchema):
    # FileStorage swagger.json

    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    template = fields.Str(required=False)
    


class PdfDefaultTemplateSuccess(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.List(fields.Nested(Document, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class StartRequest(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    params = fields.Dict(required=False)
    


class CreatedBy(BaseSchema):
    # FileStorage swagger.json

    
    username = fields.Str(required=False)
    


class CompleteResponse(BaseSchema):
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
    


class ProxyResponse(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.Dict(required=False)
    
    support = fields.Dict(required=False)
    


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
    


class SignUrlResponse(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    


class SignUrlRequest(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    urls = fields.List(fields.Str(required=False), required=False)
    


class InvoiceTypesDataResponse(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    format = fields.List(fields.Str(required=False), required=False)
    
    __v = fields.Int(required=False)
    
    visibility = fields.Boolean(required=False)
    
    store_os = fields.Boolean(required=False)
    
    country_code = fields.Str(required=False)
    


class InvoiceTypesResponse(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.List(fields.Nested(InvoiceTypesDataResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ConversionRate(BaseSchema):
    # FileStorage swagger.json

    
    base = fields.Str(required=False)
    
    rates = fields.Dict(required=False)
    
    timestamp = fields.Float(required=False)
    


class DeliveryPartnerDetail(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    awb_number_barcode = fields.Str(required=False)
    
    awb_number = fields.Str(required=False)
    
    origin = fields.Str(required=False)
    
    destination = fields.Str(required=False)
    
    eway_bill_number = fields.Str(required=False, allow_none=True)
    


class Image(BaseSchema):
    # FileStorage swagger.json

    
    sales_channel_logo = fields.Str(required=False)
    


class PaymentData(BaseSchema):
    # FileStorage swagger.json

    
    payment_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    date = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class InvoiceDetail(BaseSchema):
    # FileStorage swagger.json

    
    invoice_id = fields.Str(required=False)
    
    invoice_date = fields.Str(required=False)
    
    irn = fields.Str(required=False)
    
    external_order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    signed_qrcode = fields.Str(required=False)
    
    upi_qrcode = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    
    marketplace_invoice_id = fields.Str(required=False)
    
    marketplace_shipment_id = fields.Str(required=False)
    
    channel_order_id = fields.Str(required=False)
    


class CompanyDetail(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    zip_code = fields.Float(required=False)
    
    state_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    pan = fields.Str(required=False, allow_none=True)
    
    phone_no = fields.Str(required=False, allow_none=True)
    
    cin = fields.Str(required=False)
    
    website_url = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    phone = fields.Dict(required=False)
    
    trn = fields.Str(required=False)
    
    vat = fields.Str(required=False)
    
    business_country_timezone = fields.Str(required=False)
    
    business_country_currency = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    


class StoreDetail(BaseSchema):
    # FileStorage swagger.json

    
    store_name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    store_id = fields.Str(required=False)
    


class CustomerBillingDetail(BaseSchema):
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
    
    gstin = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class CustomerShippingDetail(BaseSchema):
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
    
    gstin = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    


class ReturnDetail(BaseSchema):
    # FileStorage swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False, allow_none=True)
    
    zip_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    


class Brand(BaseSchema):
    # FileStorage swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Cgst(BaseSchema):
    # FileStorage swagger.json

    
    value = fields.Float(required=False)
    
    percent = fields.Float(required=False)
    


class Sgst(BaseSchema):
    # FileStorage swagger.json

    
    value = fields.Float(required=False)
    
    percent = fields.Float(required=False)
    


class Igst(BaseSchema):
    # FileStorage swagger.json

    
    value = fields.Float(required=False)
    
    percent = fields.Float(required=False)
    


class Tax(BaseSchema):
    # FileStorage swagger.json

    
    cgst = fields.Nested(Cgst, required=False)
    
    sgst = fields.Nested(Sgst, required=False)
    
    igst = fields.Nested(Igst, required=False)
    


class ItemsProductTable(BaseSchema):
    # FileStorage swagger.json

    
    name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    hsn_code = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    total_units = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    mrp = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    taxable_amount = fields.Float(required=False)
    
    total_taxable_amount = fields.Float(required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    meta = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    


class ProductTable(BaseSchema):
    # FileStorage swagger.json

    
    total_items = fields.Float(required=False)
    
    products = fields.List(fields.Nested(ItemsProductTable, required=False), required=False)
    
    grand_total = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    delivery_charge_text = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    fynd_discounts = fields.Float(required=False)
    
    total_in_words = fields.Str(required=False)
    
    gift_price = fields.Float(required=False)
    
    total_quantity = fields.Float(required=False)
    
    sub_total = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    promotion = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    reward = fields.Float(required=False)
    
    round_off = fields.Float(required=False)
    
    total_value_of_goods = fields.Float(required=False)
    


class Taxes(BaseSchema):
    # FileStorage swagger.json

    
    hsn_code = fields.Str(required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    total_tax_value = fields.Float(required=False)
    


class TaxTable(BaseSchema):
    # FileStorage swagger.json

    
    taxes = fields.List(fields.Nested(Taxes, required=False), required=False)
    
    total_tax = fields.Float(required=False)
    
    tax_in_words = fields.Str(required=False)
    


class RegisteredCompanyDetail(BaseSchema):
    # FileStorage swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    zip_code = fields.Float(required=False)
    
    state_code = fields.Str(required=False)
    
    display_address = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    


class Kwargs(BaseSchema):
    # FileStorage swagger.json

    
    value = fields.Str(required=False)
    


class ShipmentIdBarcodeGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(Kwargs, required=False)
    


class SignedQrcodeGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(Kwargs, required=False)
    


class KwargsUpiQrcode(BaseSchema):
    # FileStorage swagger.json

    
    qr_data = fields.Str(required=False)
    
    qr_url = fields.Str(required=False)
    


class UpiQrcodeGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(KwargsUpiQrcode, required=False)
    


class DigitalsignatureGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(Kwargs, required=False)
    


class KwargsAwbNumber(BaseSchema):
    # FileStorage swagger.json

    
    value = fields.List(fields.Dict(required=False), required=False)
    


class AwbNumberLabelBarcodeGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(KwargsAwbNumber, required=False)
    


class AwbNumberBarcodeGenerator(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    kwargs = fields.Nested(Kwargs, required=False)
    


class MetaProperty(BaseSchema):
    # FileStorage swagger.json

    
    shipment_id_barcode_generator = fields.Nested(ShipmentIdBarcodeGenerator, required=False)
    
    signed_qrcode_generator = fields.Nested(SignedQrcodeGenerator, required=False)
    
    upi_qrcode_generator = fields.Nested(UpiQrcodeGenerator, required=False)
    
    digitalsignature_generator = fields.Nested(DigitalsignatureGenerator, required=False)
    
    awb_number_label_barcode_generator = fields.Nested(AwbNumberLabelBarcodeGenerator, required=False)
    
    awb_number_barcode_generator = fields.Nested(AwbNumberBarcodeGenerator, required=False)
    


class Meta(BaseSchema):
    # FileStorage swagger.json

    
    generator = fields.Nested(MetaProperty, required=False)
    


class DummyTemplateDataPayload(BaseSchema):
    # FileStorage swagger.json

    
    is_export = fields.Boolean(required=False)
    
    is_export_shipment = fields.Boolean(required=False)
    
    app_domain_name = fields.Str(required=False)
    
    txn_id = fields.Str(required=False)
    
    utr = fields.Str(required=False)
    
    po_number = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False, allow_none=True)
    
    current_date = fields.Str(required=False)
    
    total_value_of_goods = fields.Float(required=False)
    
    b2b_buyer_details = fields.Dict(required=False)
    
    is_qwik = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    conversion_rate = fields.Nested(ConversionRate, required=False)
    
    currency_code = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    delivery_partner_detail = fields.Nested(DeliveryPartnerDetail, required=False)
    
    image = fields.Nested(Image, required=False)
    
    payments = fields.List(fields.Nested(PaymentData, required=False), required=False)
    
    invoice_detail = fields.Nested(InvoiceDetail, required=False)
    
    company_detail = fields.Nested(CompanyDetail, required=False)
    
    store_detail = fields.Nested(StoreDetail, required=False)
    
    customer_billing_detail = fields.Nested(CustomerBillingDetail, required=False)
    
    customer_shipping_detail = fields.Nested(CustomerShippingDetail, required=False)
    
    return_detail = fields.Nested(ReturnDetail, required=False)
    
    product_table = fields.Nested(ProductTable, required=False)
    
    tax_table = fields.Nested(TaxTable, required=False)
    
    declaration_texts = fields.List(fields.Str(required=False), required=False)
    
    registered_company_detail = fields.Nested(RegisteredCompanyDetail, required=False)
    
    disclaimer = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    mode = fields.Str(required=False)
    
    is_self_pickup = fields.Boolean(required=False)
    
    platform_name = fields.Str(required=False)
    
    amount_to_be_collected = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    waybills = fields.List(fields.Dict(required=False), required=False)
    
    total_items = fields.Float(required=False)
    
    brand_logo = fields.Str(required=False)
    
    shipment_id_barcode = fields.Str(required=False)
    
    signed_qrcode = fields.Str(required=False)
    
    upi_qrcode = fields.Str(required=False)
    
    digitalsignature = fields.Str(required=False)
    
    awb_number_barcode = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class DummyTemplateData(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Float(required=False)
    
    payload = fields.Nested(DummyTemplateDataPayload, required=False)
    
    country_code = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class savePdfPayload(BaseSchema):
    # FileStorage swagger.json

    
    pdf_type_id = fields.Float(required=False)
    
    payload = fields.Nested(DummyTemplateDataPayload, required=False)
    
    country_code = fields.Str(required=False)
    


class DummyPayloadById(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Float(required=False)
    
    payload = fields.Nested(DummyTemplateDataPayload, required=False)
    
    country_code = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class DummyTemplateDataItems(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.List(fields.Nested(DummyTemplateData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    default_template = fields.Boolean(required=False)
    


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
    


class Document(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


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
    


