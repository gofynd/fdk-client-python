"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class UserSerializer(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class GetAddressSerializer(BaseSchema):
    pass


class CompanyTaxesSerializer(BaseSchema):
    pass


class Website(BaseSchema):
    pass


class BusinessDetails(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class BusinessCountryInfo(BaseSchema):
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


class CompanySocialAccounts(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class CompanySerializer(BaseSchema):
    pass


class CompanyBrandSerializer(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CompanyBrandListSerializer(BaseSchema):
    pass


class CompanyBrandPostRequestSerializer(BaseSchema):
    pass


class InvoiceCredSerializer(BaseSchema):
    pass


class InvoiceDetailsSerializer(BaseSchema):
    pass


class LocationTimingSerializer(BaseSchema):
    pass


class LocationDayWiseSerializer(BaseSchema):
    pass


class ProductReturnConfigSerializer(BaseSchema):
    pass


class GetCompanySerializer(BaseSchema):
    pass


class LocationManagerSerializer(BaseSchema):
    pass


class GetLocationSerializer(BaseSchema):
    pass


class LocationListSerializer(BaseSchema):
    pass


class LocationSerializer(BaseSchema):
    pass


class BulkLocationSerializer(BaseSchema):
    pass


class _ArticleQuery(BaseSchema):
    pass


class _ArticleAssignment(BaseSchema):
    pass


class _AssignStoreArticle(BaseSchema):
    pass


class AssignStoreRequestValidator(BaseSchema):
    pass


class AssignStoreResponseSerializer(BaseSchema):
    pass



class UserSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    contact = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class Document(BaseSchema):
    # CompanyProfile swagger.json

    
    legal_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    


class GetAddressSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    


class CompanyTaxesSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    enable = fields.Boolean(required=False)
    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    


class Website(BaseSchema):
    # CompanyProfile swagger.json

    
    url = fields.Str(required=False)
    


class BusinessDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    website = fields.Nested(Website, required=False)
    


class SellerPhoneNumber(BaseSchema):
    # CompanyProfile swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class ContactDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    emails = fields.List(fields.Str(required=False), required=False)
    
    phone = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    


class BusinessCountryInfo(BaseSchema):
    # CompanyProfile swagger.json

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    company_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_info = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    


class ErrorResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    


class CreateUpdateAddressSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    


class CompanyTaxesSerializer1(BaseSchema):
    # CompanyProfile swagger.json

    
    enable = fields.Boolean(required=False)
    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_info = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer1, required=False), required=False)
    
    name = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    


class ProfileSuccessResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class DocumentsObj(BaseSchema):
    # CompanyProfile swagger.json

    
    pending = fields.Int(required=False)
    
    verified = fields.Int(required=False)
    


class MetricsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    brand = fields.Nested(DocumentsObj, required=False)
    
    store = fields.Nested(DocumentsObj, required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    


class BrandBannerSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    


class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    description = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    


class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    brand_tier = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    


class CompanySocialAccounts(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CompanyDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    website_url = fields.Str(required=False)
    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    


class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    company_type = fields.Str(required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    created_on = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    


class Page(BaseSchema):
    # CompanyProfile swagger.json

    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    


class CompanyBrandListSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CompanyBrandPostRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    company = fields.Int(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    


class InvoiceCredSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    enabled = fields.Boolean(required=False)
    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class InvoiceDetailsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    


class LocationTimingSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class LocationDayWiseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    


class ProductReturnConfigSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    on_same_store = fields.Boolean(required=False)
    
    store_uid = fields.Int(required=False)
    


class GetCompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    created_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    company_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class LocationManagerSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    


class GetLocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    display_name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    code = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    


class LocationListSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    items = fields.List(fields.Nested(GetLocationSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    display_name = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    code = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    


class BulkLocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    data = fields.List(fields.Nested(LocationSerializer, required=False), required=False)
    


class _ArticleQuery(BaseSchema):
    # CompanyProfile swagger.json

    
    size = fields.Str(required=False)
    
    ignored_stores = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.Int(required=False)
    


class _ArticleAssignment(BaseSchema):
    # CompanyProfile swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class _AssignStoreArticle(BaseSchema):
    # CompanyProfile swagger.json

    
    quantity = fields.Int(required=False)
    
    query = fields.Nested(_ArticleQuery, required=False)
    
    group_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    


class AssignStoreRequestValidator(BaseSchema):
    # CompanyProfile swagger.json

    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    channel_type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(_AssignStoreArticle, required=False), required=False)
    


class AssignStoreResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store_pincode = fields.Str(required=False)
    
    s_city = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    preice_effective = fields.Float(required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    index = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    status = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    price_marked = fields.Float(required=False)
    


