"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class CompanyTaxesSchema(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class Website(BaseSchema):
    pass


class BusinessDetails(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class CountryCurrencyInfo(BaseSchema):
    pass


class BusinessCountryInfo(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class GetAddressSchema(BaseSchema):
    pass


class GetCompanyProfileSerializerResponseSchema(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass


class CompanyRequestTaxesSchema(BaseSchema):
    pass


class CreateUpdateAddressSchema(BaseSchema):
    pass


class UpdateCompany(BaseSchema):
    pass


class ProfileSuccessResponseSchema(BaseSchema):
    pass


class DocumentsObj(BaseSchema):
    pass


class MetricsSchema(BaseSchema):
    pass


class BrandBannerSchema(BaseSchema):
    pass


class GetBrandResponseSchema(BaseSchema):
    pass


class CreateBrandRequestSchema(BaseSchema):
    pass


class UpdateBrandRequestSchema(BaseSchema):
    pass


class CompanySocialAccounts(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class CompanySchema(BaseSchema):
    pass


class CompanyBrandSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CompanyBrandListSchema(BaseSchema):
    pass


class CompanyBrandPostRequestSchema(BaseSchema):
    pass


class InvoiceCredSchema(BaseSchema):
    pass


class InvoiceDetailsSchema(BaseSchema):
    pass


class GetCompanySchema(BaseSchema):
    pass


class LocationManagerSchema(BaseSchema):
    pass


class LocationTimingSchema(BaseSchema):
    pass


class LocationDayWiseSchema(BaseSchema):
    pass


class HolidayDateSchema(BaseSchema):
    pass


class HolidaySchemaSchema(BaseSchema):
    pass


class ProductReturnConfigSchema(BaseSchema):
    pass


class GetLocationSchema(BaseSchema):
    pass


class LocationListSchema(BaseSchema):
    pass


class AddressSchema(BaseSchema):
    pass


class LocationSchema(BaseSchema):
    pass


class BulkLocationSchema(BaseSchema):
    pass


class AverageOrderProcessingTime(BaseSchema):
    pass


class StoreTagsResponseSchema(BaseSchema):
    pass





class CompanyTaxesSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    


class UserSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class Website(BaseSchema):
    # CompanyProfile swagger.json

    
    url = fields.Str(required=False)
    


class BusinessDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    website = fields.Nested(Website, required=False)
    


class SellerPhoneNumber(BaseSchema):
    # CompanyProfile swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class ContactDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    emails = fields.List(fields.Str(required=False), required=False)
    
    phone = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    


class CountryCurrencyInfo(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class BusinessCountryInfo(BaseSchema):
    # CompanyProfile swagger.json

    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    currency = fields.Nested(CountryCurrencyInfo, required=False)
    
    timezone = fields.Str(required=False)
    


class Document(BaseSchema):
    # CompanyProfile swagger.json

    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class GetAddressSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class GetCompanyProfileSerializerResponseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    business_info = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSchema, required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    mode = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSchema, required=False), required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    


class ErrorResponseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    


class CompanyRequestTaxesSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    


class CreateUpdateAddressSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    franchise_enabled = fields.Boolean(required=False)
    
    business_info = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    company_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    taxes = fields.List(fields.Nested(CompanyRequestTaxesSchema, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSchema, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    reject_reason = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ProfileSuccessResponseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class DocumentsObj(BaseSchema):
    # CompanyProfile swagger.json

    
    pending = fields.Int(required=False)
    
    verified = fields.Int(required=False)
    


class MetricsSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    stage = fields.Str(required=False)
    
    store = fields.Nested(DocumentsObj, required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    


class BrandBannerSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    portrait = fields.Str(required=False)
    
    landscape = fields.Str(required=False)
    


class GetBrandResponseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_by = fields.Nested(UserSchema, required=False)
    
    banner = fields.Nested(BrandBannerSchema, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    slug_key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class CreateBrandRequestSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    brand_tier = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSchema, required=False)
    
    name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    


class UpdateBrandRequestSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    brand_tier = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSchema, required=False)
    
    name = fields.Str(required=False)
    


class CompanySocialAccounts(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CompanyDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    
    website_url = fields.Str(required=False)
    


class CompanySchema(BaseSchema):
    # CompanyProfile swagger.json

    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    company_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSchema, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    


class CompanyBrandSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    company = fields.Nested(CompanySchema, required=False)
    
    warnings = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSchema, required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    


class Page(BaseSchema):
    # CompanyProfile swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class CompanyBrandListSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CompanyBrandPostRequestSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    company = fields.Int(required=False)
    


class InvoiceCredSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    username = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    password = fields.Str(required=False)
    


class InvoiceDetailsSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    e_invoice = fields.Nested(InvoiceCredSchema, required=False)
    
    e_waybill = fields.Nested(InvoiceCredSchema, required=False)
    


class GetCompanySchema(BaseSchema):
    # CompanyProfile swagger.json

    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    company_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSchema, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    


class LocationManagerSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    
    name = fields.Str(required=False)
    


class LocationTimingSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class LocationDayWiseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(LocationTimingSchema, required=False)
    
    closing = fields.Nested(LocationTimingSchema, required=False)
    


class HolidayDateSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    


class HolidaySchemaSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    date = fields.Nested(HolidayDateSchema, required=False)
    
    title = fields.Str(required=False)
    
    holiday_type = fields.Str(required=False)
    


class ProductReturnConfigSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    on_same_store = fields.Boolean(required=False)
    
    store_uid = fields.Int(required=False)
    


class GetLocationSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSchema, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySchema, required=False)
    
    address = fields.Nested(GetAddressSchema, required=False)
    
    warnings = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSchema, required=False)
    
    auto_invoice = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSchema, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    credit_note = fields.Boolean(required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSchema, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSchema, required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    default_order_acceptance_timing = fields.Boolean(required=False)
    
    order_acceptance_timing = fields.List(fields.Nested(LocationDayWiseSchema, required=False), required=False)
    
    avg_order_processing_time = fields.Nested(AverageOrderProcessingTime, required=False)
    
    bulk_shipment = fields.Boolean(required=False)
    
    auto_assign_courier_partner = fields.Boolean(required=False)
    


class LocationListSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    items = fields.List(fields.Nested(GetLocationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class AddressSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class LocationSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSchema, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    warnings = fields.Dict(required=False)
    
    address = fields.Nested(AddressSchema, required=False)
    
    company = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSchema, required=False)
    
    auto_invoice = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSchema, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    credit_note = fields.Boolean(required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSchema, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSchema, required=False)
    
    display_name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    default_order_acceptance_timing = fields.Boolean(required=False)
    
    order_acceptance_timing = fields.List(fields.Nested(LocationDayWiseSchema, required=False), required=False)
    
    avg_order_processing_time = fields.Nested(AverageOrderProcessingTime, required=False)
    
    bulk_shipment = fields.Boolean(required=False)
    
    auto_assign_courier_partner = fields.Boolean(required=False)
    


class BulkLocationSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    data = fields.List(fields.Nested(LocationSchema, required=False), required=False)
    


class AverageOrderProcessingTime(BaseSchema):
    # CompanyProfile swagger.json

    
    duration = fields.Int(required=False)
    
    duration_type = fields.Str(required=False)
    


class StoreTagsResponseSchema(BaseSchema):
    # CompanyProfile swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


