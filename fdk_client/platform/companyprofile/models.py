"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class UserSerializer(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class BusinessCountryInfo(BaseSchema):
    pass


class Website(BaseSchema):
    pass


class BusinessDetails(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class GetAddressSerializer(BaseSchema):
    pass


class CompanyTaxesSerializer(BaseSchema):
    pass


class GetCompanyProfileSerializerResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class CreateUpdateAddressSerializer(BaseSchema):
    pass


class CompanyTaxesSerializer1(BaseSchema):
    pass


class UpdateCompany(BaseSchema):
    pass


class ProfileSuccessResponse(BaseSchema):
    pass


class DocumentsObj(BaseSchema):
    pass


class MetricsSerializer(BaseSchema):
    pass


class BrandBannerSerializer(BaseSchema):
    pass


class GetBrandResponseSerializer(BaseSchema):
    pass


class CreateUpdateBrandRequestSerializer(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CompanySocialAccounts(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class CompanySerializer(BaseSchema):
    pass


class CompanyBrandSerializer(BaseSchema):
    pass


class CompanyBrandListSerializer(BaseSchema):
    pass


class CompanyBrandPostRequestSerializer(BaseSchema):
    pass


class ProductReturnConfigSerializer(BaseSchema):
    pass


class LocationTimingSerializer(BaseSchema):
    pass


class LocationDayWiseSerializer(BaseSchema):
    pass


class InvoiceCredSerializer(BaseSchema):
    pass


class InvoiceDetailsSerializer(BaseSchema):
    pass


class LocationManagerSerializer(BaseSchema):
    pass


class HolidayDateSerializer(BaseSchema):
    pass


class HolidaySchemaSerializer(BaseSchema):
    pass


class GetCompanySerializer(BaseSchema):
    pass


class GetLocationSerializer(BaseSchema):
    pass


class LocationListSerializer(BaseSchema):
    pass


class AddressSerializer(BaseSchema):
    pass


class LocationSerializer(BaseSchema):
    pass


class BulkLocationSerializer(BaseSchema):
    pass





class UserSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    


class SellerPhoneNumber(BaseSchema):
    # CompanyProfile swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class ContactDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    phone = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    emails = fields.List(fields.Str(required=False), required=False)
    


class BusinessCountryInfo(BaseSchema):
    # CompanyProfile swagger.json

    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class Website(BaseSchema):
    # CompanyProfile swagger.json

    
    url = fields.Str(required=False)
    


class BusinessDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    website = fields.Nested(Website, required=False)
    


class Document(BaseSchema):
    # CompanyProfile swagger.json

    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class GetAddressSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class CompanyTaxesSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    effective_date = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    
    rate = fields.Float(required=False)
    


class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    warnings = fields.Dict(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    company_type = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_info = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    


class CreateUpdateAddressSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    country = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class CompanyTaxesSerializer1(BaseSchema):
    # CompanyProfile swagger.json

    
    effective_date = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    
    rate = fields.Float(required=False)
    


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company_type = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer1, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    business_info = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    reject_reason = fields.Str(required=False)
    


class ProfileSuccessResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    


class DocumentsObj(BaseSchema):
    # CompanyProfile swagger.json

    
    verified = fields.Int(required=False)
    
    pending = fields.Int(required=False)
    


class MetricsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store = fields.Nested(DocumentsObj, required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    


class BrandBannerSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    


class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    


class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    brand_tier = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    


class Page(BaseSchema):
    # CompanyProfile swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class CompanySocialAccounts(BaseSchema):
    # CompanyProfile swagger.json

    
    url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CompanyDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    
    website_url = fields.Str(required=False)
    


class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    stage = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    warnings = fields.Dict(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    


class CompanyBrandListSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyBrandSerializer, required=False), required=False)
    


class CompanyBrandPostRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    brands = fields.List(fields.Int(required=False), required=False)
    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    


class ProductReturnConfigSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store_uid = fields.Int(required=False)
    
    on_same_store = fields.Boolean(required=False)
    


class LocationTimingSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class LocationDayWiseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    
    weekday = fields.Str(required=False)
    


class InvoiceCredSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    enabled = fields.Boolean(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    


class InvoiceDetailsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    


class LocationManagerSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    


class HolidayDateSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class HolidaySchemaSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    date = fields.Nested(HolidayDateSerializer, required=False)
    
    holiday_type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class GetCompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    


class GetLocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    auto_invoice = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    credit_note = fields.Boolean(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    


class LocationListSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetLocationSerializer, required=False), required=False)
    


class AddressSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    auto_invoice = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    credit_note = fields.Boolean(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    address = fields.Nested(AddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    


class BulkLocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    data = fields.List(fields.Nested(LocationSerializer, required=False), required=False)
    


